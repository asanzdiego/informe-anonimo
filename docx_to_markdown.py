#!/usr/bin/env python3
"""Convert DOCX files to readable, portable Markdown without dependencies.

The converter intentionally uses only Python's standard library.  It supports
headings, inline formatting, links, lists, tables, images, notes, comments,
simple equations, tracked changes, document metadata, and headers/footers.

It is a pragmatic converter rather than a word-processing layout engine:
Markdown cannot reproduce page layout, floating objects, or every Word field.
Unsupported constructs are reported as warnings (or errors with --strict).
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import mimetypes
import os
import posixpath
import re
import shutil
import sys
import tempfile
import textwrap
import unicodedata
import urllib.parse
import zipfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Iterable, Iterator
from xml.etree import ElementTree as ET

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pr": "http://schemas.openxmlformats.org/package/2006/relationships",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "pic": "http://schemas.openxmlformats.org/drawingml/2006/picture",
    "v": "urn:schemas-microsoft-com:vml",
    "o": "urn:schemas-microsoft-com:office:office",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "ep": "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties",
    "ct": "http://schemas.openxmlformats.org/package/2006/content-types",
}

def qn(prefix: str, name: str) -> str:
    return f"{{{NS[prefix]}}}{name}"

W_VAL = qn("w", "val")
R_ID = qn("r", "id")

def attr(element: ET.Element | None, name: str, default: str = "") -> str:
    return default if element is None else element.get(W_VAL, default)

def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]

def xml_escape_attr(value: str) -> str:
    return html.escape(value, quote=True)

def slug(value: str, fallback: str = "asset") -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return value or fallback

def markdown_escape(value: str) -> str:
    """Escape characters that can unexpectedly start inline Markdown."""
    value = value.replace("\\", "\\\\")
    return re.sub(r"([`*_[\]<>])", r"\\\1", value)

def markdown_url(value: str) -> str:
    # Angle brackets keep URLs containing parentheses and spaces unambiguous.
    return "<" + value.replace("<", "%3C").replace(">", "%3E").replace(" ", "%20") + ">"

def wrap_inline(text: str, before: str, after: str | None = None) -> str:
    if not text:
        return text
    after = before if after is None else after
    match = re.match(r"^(\s*)(.*?)(\s*)$", text, re.S)
    assert match
    left, middle, right = match.groups()
    return text if not middle else f"{left}{before}{middle}{after}{right}"

def indent_block(value: str, prefix: str) -> str:
    return "\n".join(prefix + line if line else prefix.rstrip() for line in value.splitlines())

@dataclass
class Relationship:
    target: str
    external: bool = False
    rel_type: str = ""

@dataclass
class Style:
    style_id: str
    name: str = ""
    based_on: str = ""
    style_type: str = "paragraph"
    outline_level: int | None = None
    num_id: str | None = None
    ilvl: int | None = None
    formatting: dict[str, bool] = field(default_factory=dict)

@dataclass
class NumberLevel:
    level: int
    fmt: str = "bullet"
    text: str = "•"
    start: int = 1

@dataclass
class Options:
    output: Path
    assets_dir: Path
    image_mode: str = "copy"
    front_matter: bool = False
    include_deleted: bool = False
    include_comments: bool = False
    include_headers_footers: bool = False
    preserve_underline: bool = False
    hard_breaks: bool = False
    overwrite: bool = False
    strict: bool = False
    quiet: bool = False
    max_uncompressed_mb: int = 512

class ConversionError(RuntimeError):
    pass

class DocxConverter:
    def __init__(self, source: Path, options: Options):
        self.source = source
        self.options = options
        self.archive: zipfile.ZipFile | None = None
        self.names: set[str] = set()
        self.relationships: dict[str, dict[str, Relationship]] = {}
        self.styles: dict[str, Style] = {}
        self.numbering: dict[tuple[str, int], NumberLevel] = {}
        self.num_to_abstract: dict[str, str] = {}
        self.num_overrides: dict[tuple[str, int], int] = {}
        self.content_types: dict[str, str] = {}
        self.default_content_types: dict[str, str] = {}
        self.warnings: list[str] = []
        self.emitted_assets: dict[str, str] = {}
        self.used_asset_names: set[str] = set()
        self.list_counters: dict[tuple[str, int], int] = {}
        self.previous_list: tuple[str, int] | None = None
        self.footnote_refs: list[str] = []
        self.endnote_refs: list[str] = []
        self.comment_refs: list[str] = []

    def warn(self, message: str) -> None:
        if message not in self.warnings:
            self.warnings.append(message)

    def read_xml(self, name: str, required: bool = False) -> ET.Element | None:
        assert self.archive is not None
        if name not in self.names:
            if required:
                raise ConversionError(f"Falta una parte obligatoria del DOCX: {name}")
            return None
        try:
            return ET.fromstring(self.archive.read(name))
        except (ET.ParseError, KeyError) as exc:
            if required:
                raise ConversionError(f"XML no válido en {name}: {exc}") from exc
            self.warn(f"No se pudo leer {name}: {exc}")
            return None

    def validate_archive(self) -> None:
        assert self.archive is not None
        total = 0
        limit = self.options.max_uncompressed_mb * 1024 * 1024
        for info in self.archive.infolist():
            total += info.file_size
            if total > limit:
                raise ConversionError(
                    f"El contenido descomprimido supera {self.options.max_uncompressed_mb} MiB; "
                    "use --max-uncompressed-mb para cambiar el límite."
                )
            path = PurePosixPath(info.filename)
            if path.is_absolute() or ".." in path.parts:
                raise ConversionError(f"Ruta insegura dentro del DOCX: {info.filename}")
        if "word/document.xml" not in self.names:
            raise ConversionError("El archivo no contiene word/document.xml; no parece un DOCX válido.")

    def load_content_types(self) -> None:
        root = self.read_xml("[Content_Types].xml")
        if root is None:
            return
        for node in root:
            if local_name(node.tag) == "Default":
                self.default_content_types[node.get("Extension", "").lower()] = node.get("ContentType", "")
            elif local_name(node.tag) == "Override":
                self.content_types[node.get("PartName", "").lstrip("/")] = node.get("ContentType", "")

    def relationship_file(self, part: str) -> str:
        folder, filename = posixpath.split(part)
        return posixpath.join(folder, "_rels", filename + ".rels")

    def load_relationships(self, part: str) -> dict[str, Relationship]:
        if part in self.relationships:
            return self.relationships[part]
        result: dict[str, Relationship] = {}
        root = self.read_xml(self.relationship_file(part))
        if root is not None:
            for rel in root:
                rid = rel.get("Id", "")
                result[rid] = Relationship(
                    target=rel.get("Target", ""),
                    external=rel.get("TargetMode", "").lower() == "external",
                    rel_type=rel.get("Type", ""),
                )
        self.relationships[part] = result
        return result

    def resolve_relationship(self, part: str, rid: str) -> tuple[str, bool, str] | None:
        rel = self.load_relationships(part).get(rid)
        if rel is None:
            self.warn(f"Relación {rid!r} no encontrada en {part}.")
            return None
        if rel.external:
            return rel.target, True, rel.rel_type
        target = posixpath.normpath(posixpath.join(posixpath.dirname(part), rel.target))
        if target.startswith("../") or target.startswith("/"):
            self.warn(f"Se ignoró una relación con ruta insegura: {rel.target}")
            return None
        return target, False, rel.rel_type

    def load_styles(self) -> None:
        root = self.read_xml("word/styles.xml")
        if root is None:
            return
        for node in root.findall("w:style", NS):
            style_id = node.get(qn("w", "styleId"), "")
            ppr = node.find("w:pPr", NS)
            numpr = ppr.find("w:numPr", NS) if ppr is not None else None
            outline = ppr.find("w:outlineLvl", NS) if ppr is not None else None
            level = None
            if outline is not None:
                try:
                    level = int(attr(outline, "val"))
                except ValueError:
                    pass
            ilvl_node = numpr.find("w:ilvl", NS) if numpr is not None else None
            num_node = numpr.find("w:numId", NS) if numpr is not None else None
            formatting: dict[str, bool] = {}
            rpr = node.find("w:rPr", NS)
            if rpr is not None:
                for key, tags in {
                    "bold": ("b", "bCs"),
                    "italic": ("i", "iCs"),
                    "strike": ("strike", "dstrike"),
                    "underline": ("u",),
                }.items():
                    prop = next((rpr.find(f"w:{tag}", NS) for tag in tags if rpr.find(f"w:{tag}", NS) is not None), None)
                    if prop is not None:
                        formatting[key] = attr(prop, "val", "true").lower() not in {"0", "false", "off", "none"}
                vert = attr(rpr.find("w:vertAlign", NS), "val")
                if vert:
                    formatting["super"] = vert == "superscript"
                    formatting["sub"] = vert == "subscript"
            self.styles[style_id] = Style(
                style_id=style_id,
                name=attr(node.find("w:name", NS), "val", style_id),
                based_on=attr(node.find("w:basedOn", NS), "val"),
                style_type=node.get(qn("w", "type"), "paragraph"),
                outline_level=level,
                num_id=attr(num_node, "val") if num_node is not None else None,
                ilvl=int(attr(ilvl_node, "val", "0")) if ilvl_node is not None else None,
                formatting=formatting,
            )

    def style_chain(self, style_id: str) -> Iterator[Style]:
        seen: set[str] = set()
        while style_id and style_id not in seen and style_id in self.styles:
            seen.add(style_id)
            style = self.styles[style_id]
            yield style
            style_id = style.based_on

    def style_name(self, style_id: str) -> str:
        style = self.styles.get(style_id)
        return style.name if style else style_id

    def load_numbering(self) -> None:
        root = self.read_xml("word/numbering.xml")
        if root is None:
            return
        abstract_levels: dict[tuple[str, int], NumberLevel] = {}
        for abstract in root.findall("w:abstractNum", NS):
            aid = abstract.get(qn("w", "abstractNumId"), "")
            for lvl in abstract.findall("w:lvl", NS):
                try:
                    ilvl = int(lvl.get(qn("w", "ilvl"), "0"))
                    start = int(attr(lvl.find("w:start", NS), "val", "1"))
                except ValueError:
                    ilvl, start = 0, 1
                abstract_levels[(aid, ilvl)] = NumberLevel(
                    level=ilvl,
                    fmt=attr(lvl.find("w:numFmt", NS), "val", "bullet"),
                    text=attr(lvl.find("w:lvlText", NS), "val", "•"),
                    start=start,
                )
        for num in root.findall("w:num", NS):
            num_id = num.get(qn("w", "numId"), "")
            aid = attr(num.find("w:abstractNumId", NS), "val")
            self.num_to_abstract[num_id] = aid
            for override in num.findall("w:lvlOverride", NS):
                try:
                    ilvl = int(override.get(qn("w", "ilvl"), "0"))
                    start_node = override.find("w:startOverride", NS)
                    if start_node is not None:
                        self.num_overrides[(num_id, ilvl)] = int(attr(start_node, "val", "1"))
                except ValueError:
                    continue
        for num_id, aid in self.num_to_abstract.items():
            for (abstract_id, ilvl), definition in abstract_levels.items():
                if aid == abstract_id:
                    self.numbering[(num_id, ilvl)] = definition

    def core_properties(self) -> dict[str, str]:
        root = self.read_xml("docProps/core.xml")
        if root is None:
            return {}
        mapping = {
            qn("dc", "title"): "title",
            qn("dc", "subject"): "subject",
            qn("dc", "creator"): "author",
            qn("cp", "keywords"): "keywords",
            qn("dc", "description"): "description",
            qn("cp", "lastModifiedBy"): "last_modified_by",
            qn("dcterms", "created"): "created",
            qn("dcterms", "modified"): "modified",
            qn("dc", "language"): "language",
            qn("cp", "category"): "category",
        }
        result: dict[str, str] = {}
        for child in root:
            if child.tag in mapping and (child.text or "").strip():
                result[mapping[child.tag]] = (child.text or "").strip()
        return result

    def yaml_front_matter(self) -> str:
        props = self.core_properties()
        if not props:
            return ""
        lines = ["---"]
        for key, value in props.items():
            # JSON strings are valid YAML scalars and avoid a PyYAML dependency.
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
        lines.extend(["---", ""])
        return "\n".join(lines)

    def paragraph_style_id(self, paragraph: ET.Element) -> str:
        return attr(paragraph.find("w:pPr/w:pStyle", NS), "val")

    def heading_level(self, paragraph: ET.Element, style_id: str) -> int | None:
        outline = paragraph.find("w:pPr/w:outlineLvl", NS)
        if outline is not None:
            try:
                return min(6, max(1, int(attr(outline, "val")) + 1))
            except ValueError:
                pass
        for style in self.style_chain(style_id):
            if style.outline_level is not None:
                return min(6, max(1, style.outline_level + 1))
            match = re.match(r"^(?:heading|title|titulo|título)\s*([1-9])$", style.name, re.I)
            if match:
                return min(6, int(match.group(1)))
            if re.match(r"^(?:title|titulo|título)$", style.name, re.I):
                return 1
            if re.match(r"^(?:subtitle|subtitulo|subtítulo)$", style.name, re.I):
                return 2
        return None

    def list_info(self, paragraph: ET.Element, style_id: str) -> tuple[str, int] | None:
        numpr = paragraph.find("w:pPr/w:numPr", NS)
        if numpr is not None:
            num_id = attr(numpr.find("w:numId", NS), "val")
            try:
                level = int(attr(numpr.find("w:ilvl", NS), "val", "0"))
            except ValueError:
                level = 0
            if num_id and num_id != "0":
                return num_id, max(0, level)
        for style in self.style_chain(style_id):
            if style.num_id and style.num_id != "0":
                return style.num_id, style.ilvl or 0
        return None

    def list_marker(self, num_id: str, level: int) -> str:
        definition = self.numbering.get((num_id, level), NumberLevel(level))
        if definition.fmt in {"bullet", "none"}:
            return "-"
        key = (num_id, level)
        if key not in self.list_counters:
            # Word normally assigns another numId when a list restarts.
            self.list_counters[key] = self.num_overrides.get(key, definition.start) - 1
        self.list_counters[key] = self.list_counters.get(key, definition.start - 1) + 1
        for counter_key in list(self.list_counters):
            if counter_key[0] == num_id and counter_key[1] > level:
                del self.list_counters[counter_key]
        return f"{self.list_counters[key]}."

    def run_properties(self, run: ET.Element, paragraph_style: str = "") -> dict[str, bool]:
        props = run.find("w:rPr", NS)
        result = {"bold": False, "italic": False, "strike": False, "underline": False,
                  "super": False, "sub": False, "code": False, "highlight": False}

        def enabled(node: ET.Element | None) -> bool:
            return node is not None and attr(node, "val", "true").lower() not in {"0", "false", "off", "none"}

        # Paragraph and character styles can carry formatting even when a run
        # contains no direct <w:b>/<w:i> element.
        inherited: list[Style] = []
        if paragraph_style:
            inherited.extend(reversed(list(self.style_chain(paragraph_style))))
        run_style = attr(props.find("w:rStyle", NS), "val") if props is not None else ""
        if run_style:
            inherited.extend(reversed(list(self.style_chain(run_style))))
        for style in inherited:
            result.update(style.formatting)
            style_name = style.name
            if re.search(r"(?:^|\b)(strong|fuerte|negrita)(?:\b|$)", style_name, re.I):
                result["bold"] = True
            if re.search(r"(?:^|\b)(emphasis|emphasis|énfasis|enfasis)(?:\b|$)", style_name, re.I):
                result["italic"] = True
            if re.search(r"code|codigo|código|verbatim", style_name, re.I):
                result["code"] = True
        if props is not None:
            for key, tags in {
                "bold": ("b", "bCs"),
                "italic": ("i", "iCs"),
                "strike": ("strike", "dstrike"),
                "underline": ("u",),
            }.items():
                candidates = [props.find(f"w:{tag}", NS) for tag in tags]
                present = [candidate for candidate in candidates if candidate is not None]
                if present:
                    result[key] = any(enabled(candidate) for candidate in present)
            vert = attr(props.find("w:vertAlign", NS), "val")
            if vert:
                result["super"] = vert == "superscript"
                result["sub"] = vert == "subscript"
            result["highlight"] = attr(props.find("w:highlight", NS), "val") not in {"", "none"}
        return result

    def run_text(self, run: ET.Element, part: str, deleted: bool = False, paragraph_style: str = "") -> str:
        props = self.run_properties(run, paragraph_style)
        pieces: list[str] = []
        for node in run.iter():
            name = local_name(node.tag)
            if name in {"t", "delText"}:
                text = node.text or ""
                pieces.append(text if props["code"] else markdown_escape(text))
            elif name == "tab":
                pieces.append("\t")
            elif name in {"br", "cr"}:
                break_type = node.get(qn("w", "type"), "textWrapping")
                if break_type == "page":
                    pieces.append("\n\n<!-- salto de página -->\n\n")
                else:
                    pieces.append("  \n")
            elif name == "noBreakHyphen":
                pieces.append("‑")
            elif name == "softHyphen":
                pieces.append("\u00ad")
            elif name == "sym":
                code = node.get(qn("w", "char"), "")
                try:
                    pieces.append(chr(int(code, 16)))
                except (ValueError, OverflowError):
                    pass
            elif name in {"drawing", "pict", "object"}:
                pieces.extend(self.render_images(node, part))
            elif name == "footnoteReference":
                note_id = node.get(qn("w", "id"), "")
                if note_id and note_id not in self.footnote_refs:
                    self.footnote_refs.append(note_id)
                pieces.append(f"[^fn-{note_id}]")
            elif name == "endnoteReference":
                note_id = node.get(qn("w", "id"), "")
                if note_id and note_id not in self.endnote_refs:
                    self.endnote_refs.append(note_id)
                pieces.append(f"[^en-{note_id}]")
            elif name == "commentReference" and self.options.include_comments:
                comment_id = node.get(qn("w", "id"), "")
                if comment_id and comment_id not in self.comment_refs:
                    self.comment_refs.append(comment_id)
                pieces.append(f"[^comment-{comment_id}]")
        value = "".join(pieces)
        if props["code"] and value:
            fence = "``" if "`" in value else "`"
            value = wrap_inline(value, fence)
        else:
            if props["bold"] and props["italic"]:
                value = wrap_inline(value, "**")
            else:
                if props["bold"]:
                    value = wrap_inline(value, "**")
                if props["italic"]:
                    value = wrap_inline(value, "*")
            if props["strike"]:
                value = wrap_inline(value, "~~")
            if props["underline"] and self.options.preserve_underline:
                value = wrap_inline(value, "<u>", "</u>")
            if props["super"]:
                value = wrap_inline(value, "<sup>", "</sup>")
            if props["sub"]:
                value = wrap_inline(value, "<sub>", "</sub>")
            if props["highlight"]:
                value = wrap_inline(value, "<mark>", "</mark>")
        return wrap_inline(value, "~~") if deleted and value else value

    def image_alt(self, node: ET.Element) -> str:
        for tag in ("wp:docPr", "pic:cNvPr"):
            item = node.find(f".//{tag}", NS)
            if item is not None:
                value = item.get("descr") or item.get("title") or item.get("name")
                if value:
                    return value
        return "imagen"

    def render_images(self, node: ET.Element, part: str) -> list[str]:
        results: list[str] = []
        seen: set[str] = set()
        candidates: list[tuple[str, str]] = []
        for blip in node.findall(".//a:blip", NS):
            rid = blip.get(qn("r", "embed")) or blip.get(qn("r", "link"))
            if rid:
                candidates.append((rid, self.image_alt(node)))
        for image_data in node.findall(".//v:imagedata", NS):
            rid = image_data.get(R_ID)
            if rid:
                candidates.append((rid, image_data.get(qn("o", "title"), "") or self.image_alt(node)))
        for rid, alt_text in candidates:
            if rid in seen:
                continue
            seen.add(rid)
            resolved = self.resolve_relationship(part, rid)
            if resolved is None:
                continue
            target, external, _ = resolved
            if self.options.image_mode == "ignore":
                continue
            if external:
                results.append(f"![{markdown_escape(alt_text)}]({markdown_url(target)})")
                continue
            uri = self.emit_asset(target)
            if uri:
                results.append(f"![{markdown_escape(alt_text)}]({markdown_url(uri)})")
        return results

    def content_type_for(self, part: str) -> str:
        return self.content_types.get(part) or self.default_content_types.get(Path(part).suffix.lstrip(".").lower()) \
            or mimetypes.guess_type(part)[0] or "application/octet-stream"

    def emit_asset(self, part: str) -> str:
        if part in self.emitted_assets:
            return self.emitted_assets[part]
        assert self.archive is not None
        if part not in self.names:
            self.warn(f"Recurso incrustado no encontrado: {part}")
            return ""
        data = self.archive.read(part)
        mime = self.content_type_for(part)
        if self.options.image_mode == "embed":
            uri = f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"
            self.emitted_assets[part] = uri
            return uri
        original = Path(part).name
        stem, suffix = slug(Path(original).stem), Path(original).suffix.lower()
        candidate = stem + suffix
        if candidate in self.used_asset_names:
            candidate = f"{stem}-{hashlib.sha256(data).hexdigest()[:8]}{suffix}"
        self.used_asset_names.add(candidate)
        destination = self.options.assets_dir / candidate
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and destination.read_bytes() != data:
            candidate = f"{stem}-{hashlib.sha256(data).hexdigest()[:12]}{suffix}"
            destination = self.options.assets_dir / candidate
        destination.write_bytes(data)
        try:
            relative = os.path.relpath(destination, self.options.output.parent)
        except ValueError:
            relative = str(destination)
        uri = Path(relative).as_posix()
        self.emitted_assets[part] = uri
        return uri

    def field_hyperlink(self, instruction: str) -> str:
        match = re.search(r'HYPERLINK\s+(?:"([^"]+)"|(\S+))', instruction, re.I)
        return (match.group(1) or match.group(2)) if match else ""

    def render_hyperlink(self, node: ET.Element, part: str, paragraph_style: str = "") -> str:
        label = self.render_inline_children(node, part, paragraph_style=paragraph_style).strip()
        anchor = node.get(qn("w", "anchor"), "")
        rid = node.get(R_ID, "")
        target = "#" + urllib.parse.quote(anchor) if anchor else ""
        if rid:
            resolved = self.resolve_relationship(part, rid)
            if resolved:
                target = resolved[0]
        if not target:
            return label
        return f"[{label or markdown_escape(target)}]({markdown_url(target)})"

    def math_to_text(self, node: ET.Element) -> str:
        name = local_name(node.tag)
        if name == "t":
            return node.text or ""
        children = list(node)
        if name == "f":
            num = node.find("m:num", NS)
            den = node.find("m:den", NS)
            return rf"\frac{{{self.math_to_text(num) if num is not None else ''}}}{{{self.math_to_text(den) if den is not None else ''}}}"
        if name == "sSup":
            base, sup = node.find("m:e", NS), node.find("m:sup", NS)
            return f"{self.math_to_text(base) if base is not None else ''}^{{{self.math_to_text(sup) if sup is not None else ''}}}"
        if name == "sSub":
            base, sub = node.find("m:e", NS), node.find("m:sub", NS)
            return f"{self.math_to_text(base) if base is not None else ''}_{{{self.math_to_text(sub) if sub is not None else ''}}}"
        if name == "rad":
            degree, expr = node.find("m:deg", NS), node.find("m:e", NS)
            degree_text = self.math_to_text(degree) if degree is not None else ""
            command = rf"\sqrt[{degree_text}]" if degree_text else r"\sqrt"
            return f"{command}{{{self.math_to_text(expr) if expr is not None else ''}}}"
        if name == "nary":
            char = attr(node.find("m:naryPr/m:chr", NS), "val", "∑")
            commands = {"∑": r"\sum", "∏": r"\prod", "∫": r"\int"}
            return commands.get(char, char) + "".join(self.math_to_text(c) for c in children if local_name(c.tag) != "naryPr")
        if name in {"d", "groupChr"}:
            return "(" + "".join(self.math_to_text(c) for c in children if local_name(c.tag) not in {"dPr", "groupChrPr"}) + ")"
        return "".join(self.math_to_text(child) for child in children if not local_name(child.tag).endswith("Pr"))

    def render_inline_children(
        self, parent: ET.Element, part: str, deleted: bool = False, paragraph_style: str = ""
    ) -> str:
        pieces: list[str] = []
        for child in parent:
            name = local_name(child.tag)
            if name in {"pPr", "rPr", "proofErr", "permStart", "permEnd", "commentRangeStart", "commentRangeEnd"}:
                continue
            if name == "r":
                pieces.append(self.run_text(child, part, deleted, paragraph_style))
            elif name == "hyperlink":
                pieces.append(self.render_hyperlink(child, part, paragraph_style))
            elif name == "fldSimple":
                label = self.render_inline_children(child, part, paragraph_style=paragraph_style)
                target = self.field_hyperlink(child.get(qn("w", "instr"), ""))
                pieces.append(f"[{label}]({markdown_url(target)})" if target else label)
            elif name in {"ins", "moveTo"}:
                pieces.append(self.render_inline_children(child, part, paragraph_style=paragraph_style))
            elif name in {"del", "moveFrom"}:
                if self.options.include_deleted:
                    pieces.append(self.render_inline_children(child, part, deleted=True, paragraph_style=paragraph_style))
            elif name in {"smartTag", "sdt", "customXml", "dir", "bdo"}:
                content = child.find("w:sdtContent", NS) if name == "sdt" else child
                if content is not None:
                    pieces.append(self.render_inline_children(content, part, deleted, paragraph_style))
            elif name in {"oMath", "oMathPara"}:
                equation = self.math_to_text(child).strip()
                if equation:
                    pieces.append(f"${equation}$")
            elif name == "bookmarkStart":
                bookmark = child.get(qn("w", "name"), "")
                if bookmark and not bookmark.startswith("_"):
                    pieces.append(f'<a id="{xml_escape_attr(bookmark)}"></a>')
            elif name == "altChunk":
                self.warn("Se encontró contenido altChunk que no se puede representar sin un motor de Word.")
            else:
                pieces.append(self.render_inline_children(child, part, deleted, paragraph_style))
        return "".join(pieces)

    def render_paragraph(self, paragraph: ET.Element, part: str, in_cell: bool = False) -> str:
        style_id = self.paragraph_style_id(paragraph)
        style_name = self.style_name(style_id)
        level = self.heading_level(paragraph, style_id)
        # Bold/italic inherited from a heading style are redundant in Markdown;
        # direct run formatting and character styles are still preserved.
        inherited_style = "" if level is not None else style_id
        value = self.render_inline_children(paragraph, part, paragraph_style=inherited_style).strip(" \t")
        if not value:
            self.previous_list = None
            return ""
        if level is not None:
            self.previous_list = None
            return f"{'#' * level} {value}"
        list_info = self.list_info(paragraph, style_id)
        if list_info:
            num_id, ilvl = list_info
            marker = self.list_marker(num_id, ilvl)
            self.previous_list = (num_id, ilvl)
            continuation = " " * (ilvl * 4 + len(marker) + 1)
            lines = value.splitlines()
            rendered = " " * (ilvl * 4) + marker + " " + lines[0]
            if len(lines) > 1:
                rendered += "\n" + "\n".join(continuation + line for line in lines[1:])
            return rendered
        self.previous_list = None
        if re.search(r"(?:quote|quotation|citation|cita|citación)", style_name, re.I):
            return indent_block(value, "> ")
        if re.search(r"(?:code|codigo|código|preformatted|preformateado)", style_name, re.I):
            fence = "````" if "```" in value else "```"
            return f"{fence}\n{value}\n{fence}"
        if self.options.hard_breaks and not in_cell:
            value = re.sub(r"(?<!  )\n", "  \n", value)
        return value

    def cell_blocks(self, cell: ET.Element, part: str) -> list[str]:
        return [block for child in cell if (block := self.render_block(child, part, in_cell=True))]

    def table_has_merges(self, table: ET.Element) -> bool:
        return table.find(".//w:gridSpan", NS) is not None or table.find(".//w:vMerge", NS) is not None

    def render_markdown_table(self, table: ET.Element, part: str) -> str:
        rows: list[list[str]] = []
        max_columns = 0
        for tr in table.findall("w:tr", NS):
            row: list[str] = []
            for tc in tr.findall("w:tc", NS):
                cell = "<br>".join(self.cell_blocks(tc, part)).replace("|", r"\|")
                cell = re.sub(r"\s*\n\s*", "<br>", cell).strip()
                row.append(cell)
            max_columns = max(max_columns, len(row))
            rows.append(row)
        if not rows or not max_columns:
            return ""
        for row in rows:
            row.extend([""] * (max_columns - len(row)))
        output = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * max_columns) + " |"]
        output.extend("| " + " | ".join(row) + " |" for row in rows[1:])
        return "\n".join(output)

    def inline_markdown_to_html(self, value: str) -> str:
        """Translate the Markdown generated by this class for an HTML cell."""
        held: dict[str, str] = {}

        def hold(rendered: str) -> str:
            token = f"DOCXHTMLTOKEN{len(held)}X"
            held[token] = rendered
            return token

        def image_to_html(match: re.Match[str]) -> str:
            alt_text = re.sub(r"[\\*_~`]", "", match.group(1))
            return hold(
                f'<img src="{xml_escape_attr(match.group(2))}" '
                f'alt="{xml_escape_attr(alt_text)}">'
            )

        # Protect constructs whose attributes and contents need independent
        # escaping before escaping the remaining plain text.
        image_re = re.compile(r"!\[([^]]*)\]\(<([^>]*)>\)")
        value = image_re.sub(image_to_html, value)
        link_re = re.compile(r"\[([^]]*)\]\(<([^>]*)>\)")
        value = link_re.sub(
            lambda match: hold(
                f'<a href="{xml_escape_attr(match.group(2))}">'
                f'{self.inline_markdown_to_html(match.group(1))}</a>'
            ),
            value,
        )
        value = re.sub(
            r"<(?:/?(?:u|sup|sub|mark)|br)>|<a id=\"[^\"]*\"></a>|<!-- salto de página -->",
            lambda match: hold(match.group(0)),
            value,
        )
        # Escaped Markdown punctuation is literal, not formatting.
        value = re.sub(
            r"\\([\\`*_\[\]<>])",
            lambda match: hold(html.escape(match.group(1))),
            value,
        )
        value = html.escape(value, quote=False)
        value = re.sub(r"(?<!\\)\*\*\*(.+?)(?<!\\)\*\*\*", r"<strong><em>\1</em></strong>", value)
        value = re.sub(r"(?<!\\)\*\*(.+?)(?<!\\)\*\*", r"<strong>\1</strong>", value)
        value = re.sub(r"(?<!\\)~~(.+?)(?<!\\)~~", r"<del>\1</del>", value)
        value = re.sub(r"(?<!\\)\*(.+?)(?<!\\)\*", r"<em>\1</em>", value)
        value = re.sub(r"(?<!\\)`([^`]+)`", r"<code>\1</code>", value)
        value = value.replace("  \n", "<br>").replace("\n", "<br>")
        for token, rendered in held.items():
            value = value.replace(token, rendered)
        return value

    def render_html_table(self, table: ET.Element, part: str) -> str:
        rows_data: list[list[dict[str, object]]] = []
        active: dict[int, dict[str, object]] = {}
        for row_index, tr in enumerate(table.findall("w:tr", NS)):
            row: list[dict[str, object]] = []
            col = 0
            for tc in tr.findall("w:tc", NS):
                tcpr = tc.find("w:tcPr", NS)
                try:
                    colspan = int(attr(tcpr.find("w:gridSpan", NS) if tcpr is not None else None, "val", "1"))
                except ValueError:
                    colspan = 1
                merge = tcpr.find("w:vMerge", NS) if tcpr is not None else None
                merge_value = attr(merge, "val", "continue") if merge is not None else ""
                if merge is not None and merge_value != "restart" and col in active:
                    origin = active[col]
                    origin["rowspan"] = int(origin.get("rowspan", 1)) + 1
                else:
                    cell: dict[str, object] = {
                        "text": "<br>".join(self.cell_blocks(tc, part)),
                        "colspan": colspan,
                        "rowspan": 1,
                        "header": row_index == 0,
                    }
                    row.append(cell)
                    if merge_value == "restart":
                        for c in range(col, col + colspan):
                            active[c] = cell
                    else:
                        for c in range(col, col + colspan):
                            active.pop(c, None)
                col += colspan
            rows_data.append(row)
        lines = ["<table>"]
        for row in rows_data:
            lines.append("  <tr>")
            for cell in row:
                tag = "th" if cell["header"] else "td"
                attrs = ""
                if int(cell["colspan"]) > 1:
                    attrs += f' colspan="{cell["colspan"]}"'
                if int(cell["rowspan"]) > 1:
                    attrs += f' rowspan="{cell["rowspan"]}"'
                # Inline Markdown inside HTML is inconsistently parsed, so the
                # cell content is kept readable and minimally HTML-safe.
                value = self.inline_markdown_to_html(str(cell["text"]))
                lines.append(f"    <{tag}{attrs}>{value}</{tag}>")
            lines.append("  </tr>")
        lines.append("</table>")
        return "\n".join(lines)

    def render_table(self, table: ET.Element, part: str) -> str:
        if self.table_has_merges(table):
            return self.render_html_table(table, part)
        return self.render_markdown_table(table, part)

    def render_block(self, node: ET.Element, part: str, in_cell: bool = False) -> str:
        name = local_name(node.tag)
        if name == "p":
            return self.render_paragraph(node, part, in_cell)
        if name == "tbl":
            self.previous_list = None
            return self.render_table(node, part)
        if name == "sdt":
            content = node.find("w:sdtContent", NS)
            return self.render_blocks(content if content is not None else node, part, in_cell)
        if name in {"ins", "moveTo"}:
            return self.render_blocks(node, part, in_cell)
        if name in {"del", "moveFrom"} and self.options.include_deleted:
            return self.render_blocks(node, part, in_cell)
        if name == "altChunk":
            self.warn("Se omitió un bloque altChunk (HTML/RTF incrustado).")
        return ""

    def render_blocks(self, parent: ET.Element, part: str, in_cell: bool = False) -> str:
        blocks: list[str] = []
        for child in parent:
            value = self.render_block(child, part, in_cell)
            if value:
                blocks.append(value)
        return "\n\n".join(blocks)

    def render_notes(self, part: str, tag: str, references: list[str], prefix: str) -> str:
        root = self.read_xml(part)
        if root is None or not references:
            return ""
        by_id = {node.get(qn("w", "id"), ""): node for node in root.findall(f"w:{tag}", NS)}
        definitions: list[str] = []
        for note_id in references:
            node = by_id.get(note_id)
            if node is None:
                self.warn(f"No se encontró la nota {note_id} en {part}.")
                continue
            text = self.render_blocks(node, part).strip()
            text = re.sub(r"^\[\^(?:fn|en)-[^]]+\]\s*", "", text)
            lines = text.splitlines() or [""]
            definitions.append(f"[^{prefix}-{note_id}]: {lines[0]}" + (
                "\n" + "\n".join("    " + line for line in lines[1:]) if len(lines) > 1 else ""
            ))
        return "\n\n".join(definitions)

    def render_comments(self) -> str:
        root = self.read_xml("word/comments.xml")
        if root is None or not self.comment_refs:
            return ""
        by_id = {node.get(qn("w", "id"), ""): node for node in root.findall("w:comment", NS)}
        definitions: list[str] = []
        for comment_id in self.comment_refs:
            node = by_id.get(comment_id)
            if node is None:
                continue
            author = node.get(qn("w", "author"), "").strip()
            date = node.get(qn("w", "date"), "").strip()
            label = " — ".join(x for x in (author, date) if x)
            text = self.render_blocks(node, "word/comments.xml").strip()
            if label:
                text = f"{text} ({markdown_escape(label)})"
            lines = text.splitlines() or [""]
            definitions.append(f"[^comment-{comment_id}]: {lines[0]}" + (
                "\n" + "\n".join("    " + line for line in lines[1:]) if len(lines) > 1 else ""
            ))
        return "\n\n".join(definitions)

    def render_headers_footers(self, document: ET.Element) -> str:
        if not self.options.include_headers_footers:
            return ""
        sections: list[str] = []
        seen_parts: set[str] = set()
        for reference in document.findall(".//w:sectPr/*", NS):
            name = local_name(reference.tag)
            if name not in {"headerReference", "footerReference"}:
                continue
            rid = reference.get(R_ID, "")
            resolved = self.resolve_relationship("word/document.xml", rid)
            if not resolved or resolved[1] or resolved[0] in seen_parts:
                continue
            target = resolved[0]
            seen_parts.add(target)
            root = self.read_xml(target)
            if root is None:
                continue
            content = self.render_blocks(root, target).strip()
            if content:
                label = "Encabezado" if name == "headerReference" else "Pie de página"
                kind = reference.get(qn("w", "type"), "default")
                sections.append(f"### {label} ({kind})\n\n{content}")
        return "\n\n".join(sections)

    def convert(self) -> tuple[str, list[str]]:
        try:
            self.archive = zipfile.ZipFile(self.source)
        except (OSError, zipfile.BadZipFile) as exc:
            raise ConversionError(f"No se pudo abrir {self.source}: {exc}") from exc
        with self.archive:
            self.names = set(self.archive.namelist())
            self.validate_archive()
            self.load_content_types()
            self.load_styles()
            self.load_numbering()
            document = self.read_xml("word/document.xml", required=True)
            assert document is not None
            body = document.find("w:body", NS)
            if body is None:
                raise ConversionError("word/document.xml no contiene un cuerpo de documento.")
            chunks: list[str] = []
            if self.options.front_matter:
                front = self.yaml_front_matter().strip()
                if front:
                    chunks.append(front)
            main = self.render_blocks(body, "word/document.xml").strip()
            if main:
                chunks.append(main)
            # Render these first so references appearing in a header/footer are
            # also present when note/comment definitions are collected.
            headers = self.render_headers_footers(document)
            footnotes = self.render_notes("word/footnotes.xml", "footnote", self.footnote_refs, "fn")
            endnotes = self.render_notes("word/endnotes.xml", "endnote", self.endnote_refs, "en")
            comments = self.render_comments() if self.options.include_comments else ""
            if footnotes:
                chunks.append(footnotes)
            if endnotes:
                chunks.append(endnotes)
            if comments:
                chunks.append(comments)
            if headers:
                chunks.append("## Encabezados y pies de página\n\n" + headers)
            markdown = "\n\n".join(chunk.strip() for chunk in chunks if chunk.strip())
            markdown = re.sub(r"\n{3,}", "\n\n", markdown).rstrip() + "\n"
            return markdown, self.warnings

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convierte un archivo DOCX a Markdown sin dependencias externas.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
            Ejemplos:
              %(prog)s informe.docx
              %(prog)s informe.docx -o README.md --front-matter
              %(prog)s informe.docx --image-mode embed --overwrite
              %(prog)s cambios.docx --include-deleted --include-comments

            Limitaciones:
              Markdown no conserva maquetación de página, formas flotantes, gráficos
              editables, macros ni todos los campos automáticos de Microsoft Word.
        """),
    )
    parser.add_argument("input", type=Path, help="archivo DOCX de entrada")
    parser.add_argument("-o", "--output", type=Path, help="archivo Markdown de salida (por defecto: mismo nombre con .md)")
    parser.add_argument("--assets-dir", type=Path, help="carpeta para imágenes (por defecto: <salida>_assets)")
    parser.add_argument("--image-mode", choices=("copy", "embed", "ignore"), default="copy",
                        help="copiar, incrustar como data URI u omitir imágenes (por defecto: copy)")
    parser.add_argument("--front-matter", action="store_true", help="añadir metadatos DOCX como front matter YAML")
    parser.add_argument("--include-deleted", action="store_true", help="incluir texto eliminado por control de cambios, tachado")
    parser.add_argument("--include-comments", action="store_true", help="incluir comentarios de Word como notas Markdown")
    parser.add_argument("--include-headers-footers", action="store_true", help="añadir encabezados y pies al final")
    parser.add_argument("--preserve-underline", action="store_true", help="conservar subrayado mediante etiquetas HTML <u>")
    parser.add_argument("--hard-breaks", action="store_true", help="convertir saltos internos de párrafo en saltos Markdown duros")
    parser.add_argument("--overwrite", action="store_true", help="sobrescribir el archivo de salida si ya existe")
    parser.add_argument("--strict", action="store_true", help="considerar cualquier advertencia como error")
    parser.add_argument("--quiet", action="store_true", help="no mostrar mensajes informativos")
    parser.add_argument("--max-uncompressed-mb", type=int, default=512, metavar="MB",
                        help="límite de seguridad del DOCX descomprimido (por defecto: 512)")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")
    return parser

def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise

def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    source = args.input.expanduser().resolve()
    if not source.is_file():
        parser.error(f"no existe el archivo de entrada: {source}")
    if source.suffix.lower() != ".docx":
        parser.error("el archivo de entrada debe tener extensión .docx")
    if args.max_uncompressed_mb < 1:
        parser.error("--max-uncompressed-mb debe ser mayor que cero")
    output = (args.output or source.with_suffix(".md")).expanduser().resolve()
    if output == source:
        parser.error("la salida no puede ser el mismo archivo que la entrada")
    if output.exists() and not args.overwrite:
        parser.error(f"la salida ya existe: {output} (use --overwrite)")
    default_assets = output.parent / f"{output.stem}_assets"
    assets_dir = (args.assets_dir or default_assets).expanduser().resolve()
    options = Options(
        output=output,
        assets_dir=assets_dir,
        image_mode=args.image_mode,
        front_matter=args.front_matter,
        include_deleted=args.include_deleted,
        include_comments=args.include_comments,
        include_headers_footers=args.include_headers_footers,
        preserve_underline=args.preserve_underline,
        hard_breaks=args.hard_breaks,
        overwrite=args.overwrite,
        strict=args.strict,
        quiet=args.quiet,
        max_uncompressed_mb=args.max_uncompressed_mb,
    )
    try:
        converter = DocxConverter(source, options)
        markdown, warnings = converter.convert()
        if args.strict and warnings:
            raise ConversionError("Conversión detenida por --strict:\n- " + "\n- ".join(warnings))
        write_atomic(output, markdown)
    except (ConversionError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    if not args.quiet:
        print(f"Creado: {output}", file=sys.stderr)
        if args.image_mode == "copy" and converter.emitted_assets:
            print(f"Recursos: {assets_dir} ({len(converter.emitted_assets)})", file=sys.stderr)
        for warning in warnings:
            print(f"Advertencia: {warning}", file=sys.stderr)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
