#!/usr/bin/env python3
"""Convert PDF files to clean, portable Markdown.

The script deliberately supports several extraction engines so that it remains
useful in very different environments:

* PyMuPDF (recommended): layout, font-based headings, links, tables and images.
* pypdf: dependency-light text, metadata, links and embedded images.
* pdftotext: command-line fallback with good text extraction.

Scanned pages can be recognized with the optional ``tesseract`` executable.
No network service is used.  A PDF is a fixed-layout output format, so reading
order and complex tables can only be reconstructed heuristically.

Recommended installation::

    python -m pip install pymupdf
    # Debian/Ubuntu, only for OCR:
    sudo apt install tesseract-ocr tesseract-ocr-spa

The program itself is a single file and does not require a requirements file.
Run ``python pdf_to_markdown.py --help`` for all options.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import importlib
import json
import math
import os
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import textwrap
import unicodedata
import urllib.parse
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Sequence

VERSION = "1.0.0"
LIST_RE = re.compile(r"^\s*(?:[-*+•◦▪‣]\s+|\(?\d{1,4}[.)]\s+|[A-Za-z][.)]\s+)")
NUMBERED_HEADING_RE = re.compile(r"^\s*(?:\d+(?:\.\d+){0,5}|[IVXLCDM]+)[.)]?\s+\S", re.I)
PAGE_NUMBER_RE = re.compile(r"^\s*(?:p(?:á|a)g(?:ina)?\.?\s*)?[-–—]?\s*\d+\s*(?:/|de)\s*\d+\s*[-–—]?\s*$|^\s*[-–—]?\s*\d+\s*[-–—]?\s*$", re.I)
URI_RE = re.compile(r"^(?:https?://|mailto:)", re.I)

class ConversionError(RuntimeError):
    """A user-facing conversion failure."""

@dataclass
class Options:
    output: Path
    assets_dir: Path
    engine: str = "auto"
    pages: str = "all"
    password: str = ""
    images: str = "copy"
    tables: bool = True
    ocr: str = "auto"
    ocr_language: str = "spa+eng"
    ocr_dpi: int = 300
    ocr_psm: int = 1
    ocr_min_chars: int = 40
    page_markers: str = "comment"
    front_matter: bool = False
    toc: bool = False
    preserve_line_breaks: bool = False
    keep_headers_footers: bool = False
    dehyphenate: bool = True
    min_image_width: int = 80
    min_image_height: int = 80
    max_file_mb: int = 1024
    max_pages: int = 5000
    timeout: int = 120
    overwrite: bool = False
    strict: bool = False
    quiet: bool = False

@dataclass
class Element:
    y: float
    x: float
    kind: str
    content: str
    bbox: tuple[float, float, float, float] | None = None

@dataclass
class PageResult:
    number: int
    markdown: str
    raw_text: str
    warnings: list[str] = field(default_factory=list)

def executable(name: str) -> str | None:
    return shutil.which(name)

def optional_import(*names: str) -> Any | None:
    for name in names:
        try:
            return importlib.import_module(name)
        except (ImportError, RuntimeError):
            continue
    return None

def markdown_escape(value: str) -> str:
    value = value.replace("\\", "\\\\")
    return re.sub(r"([`*_[\]<>|])", r"\\\1", value)

def markdown_url(value: str) -> str:
    return "<" + value.replace("<", "%3C").replace(">", "%3E").replace(" ", "%20") + ">"

def clean_text(value: str) -> str:
    value = unicodedata.normalize("NFC", value or "")
    # Some PDF encodings expose a bullet as DEL (U+007F), notably through
    # pypdf.  Recover it before stripping control characters.
    value = value.replace("\x7f", "•")
    value = value.replace("\u00ad", "").replace("\u00a0", " ").replace("\u200b", "")
    value = "".join(ch for ch in value if ch in "\n\t" or unicodedata.category(ch) != "Cc")
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r" *\n *", "\n", value)
    return value.strip()

def clean_inline_text(value: str) -> str:
    """Clean a span without losing separators around formatting changes."""
    if not value:
        return ""
    leading = " " if value[0].isspace() else ""
    trailing = " " if value[-1].isspace() else ""
    middle = clean_text(value)
    if not middle:
        return " " if leading or trailing else ""
    return leading + middle + trailing

def yaml_string(value: Any) -> str:
    return json.dumps(str(value), ensure_ascii=False)

def rectangle_intersection_ratio(
    first: Sequence[float], second: Sequence[float]
) -> float:
    x0 = max(float(first[0]), float(second[0]))
    y0 = max(float(first[1]), float(second[1]))
    x1 = min(float(first[2]), float(second[2]))
    y1 = min(float(first[3]), float(second[3]))
    intersection = max(0.0, x1 - x0) * max(0.0, y1 - y0)
    area = max(1.0, (float(first[2]) - float(first[0])) * (float(first[3]) - float(first[1])))
    return intersection / area

def parse_page_spec(spec: str, total: int) -> list[int]:
    """Return zero-based page indexes for expressions such as 1-3,5,8-."""
    if total < 1:
        return []
    if not spec or spec.lower() in {"all", "todas", "*"}:
        return list(range(total))
    selected: set[int] = set()
    for item in spec.split(","):
        item = item.strip()
        if not item:
            raise ConversionError(f"Selección de páginas no válida: {spec!r}")
        match = re.fullmatch(r"(\d*)\s*-\s*(\d*)", item)
        if match:
            start_text, end_text = match.groups()
            if not start_text and not end_text:
                raise ConversionError(f"Rango de páginas vacío: {item!r}")
            start = int(start_text) if start_text else 1
            end = int(end_text) if end_text else total
            if start < 1 or end < 1 or start > end:
                raise ConversionError(f"Rango de páginas no válido: {item!r}")
            if start > total or end > total:
                raise ConversionError(f"El rango {item!r} excede las {total} páginas del PDF")
            selected.update(range(start - 1, end))
        elif item.isdigit():
            page = int(item)
            if page < 1 or page > total:
                raise ConversionError(f"La página {page} no existe (el PDF tiene {total})")
            selected.add(page - 1)
        else:
            raise ConversionError(f"Selección de páginas no válida: {item!r}")
    return sorted(selected)

def table_to_markdown(rows: Iterable[Iterable[Any]]) -> str:
    normalized: list[list[str]] = []
    for row in rows:
        cells: list[str] = []
        for value in row:
            cell = clean_text("" if value is None else str(value)).replace("\n", "<br>")
            cells.append(markdown_escape(cell))
        normalized.append(cells)
    if not normalized:
        return ""
    columns = max(len(row) for row in normalized)
    if columns == 0:
        return ""
    normalized = [row + [""] * (columns - len(row)) for row in normalized]
    header = normalized[0]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    lines.extend("| " + " | ".join(row) + " |" for row in normalized[1:])
    return "\n".join(lines)

def join_wrapped_lines(lines: Iterable[str], dehyphenate: bool = True) -> str:
    """Turn visual PDF lines into paragraphs while preserving obvious lists."""
    output: list[str] = []
    paragraph = ""

    def flush() -> None:
        nonlocal paragraph
        if paragraph.strip():
            output.append(paragraph.strip())
        paragraph = ""

    for original in lines:
        line = clean_text(original)
        if not line:
            flush()
            if output and output[-1] != "":
                output.append("")
            continue
        if LIST_RE.match(line):
            flush()
            line = re.sub(r"^\s*[•◦▪‣]\s+", "- ", line)
            output.append(line)
            continue
        if line.startswith(("#", ">", "```", "| ")):
            flush()
            output.append(line)
            continue
        if paragraph:
            if dehyphenate and re.search(r"\w-$", paragraph) and re.match(r"^[a-záéíóúüñ]", line):
                paragraph = paragraph[:-1] + line
            else:
                paragraph += " " + line
        else:
            paragraph = line
    flush()
    result = "\n".join(output)
    return re.sub(r"\n{3,}", "\n\n", result).strip()

def plain_text_to_markdown(text: str, options: Options) -> str:
    text = clean_text(text)
    if not text:
        return ""
    lines: list[str] = []
    source_lines = text.splitlines()
    for index, source_line in enumerate(source_lines):
        line = source_line.strip()
        if not line:
            lines.append("")
            continue
        isolated = (
            (index == 0 or not source_lines[index - 1].strip())
            and (index == len(source_lines) - 1 or not source_lines[index + 1].strip())
        )
        # A numbered line surrounded by vertical whitespace is much more
        # likely to be a section title than an ordered-list item.
        if (isolated and len(line) <= 120 and NUMBERED_HEADING_RE.match(line)
                and not line.endswith((".", ";", ","))):
            lines.append("## " + markdown_escape(line))
            continue
        if LIST_RE.match(line):
            line = re.sub(r"^\s*[•◦▪‣]\s+", "- ", line)
            lines.append(markdown_escape(line) if not line.startswith("- ") else "- " + markdown_escape(line[2:]))
            continue
        # Conservative heading inference for engines without font information.
        letters = [char for char in line if char.isalpha()]
        uppercase = bool(letters) and sum(char.isupper() for char in letters) / len(letters) > 0.9
        if len(line) <= 90 and uppercase and len(letters) >= 4:
            lines.append("### " + markdown_escape(line))
        else:
            lines.append(markdown_escape(line))
    if options.preserve_line_breaks:
        return "  \n".join(lines).replace("  \n  \n", "\n\n").strip()
    return join_wrapped_lines(lines, options.dehyphenate)

def normalize_repeated_line(value: str) -> str:
    value = clean_text(value).casefold()
    return re.sub(r"\s+", " ", value)

def remove_repeated_headers_footers(pages: list[PageResult]) -> None:
    if len(pages) < 2:
        return
    candidates: Counter[str] = Counter()
    page_lines: dict[int, tuple[list[str], list[str]]] = {}
    for page in pages:
        nonempty = [line.strip() for line in page.raw_text.splitlines() if line.strip()]
        first, last = nonempty[:2], nonempty[-2:]
        page_lines[page.number] = (first, last)
        candidates.update(set(normalize_repeated_line(line) for line in first + last))
    threshold = max(2, math.ceil(len(pages) * 0.5))
    repeated = {line for line, count in candidates.items() if line and count >= threshold}
    for page in pages:
        first, last = page_lines[page.number]
        removable = {
            line for line in first + last
            if normalize_repeated_line(line) in repeated or PAGE_NUMBER_RE.match(line)
        }
        if not removable:
            continue
        raw_lines = page.raw_text.splitlines()
        md_lines = page.markdown.splitlines()
        page.raw_text = "\n".join(line for line in raw_lines if line.strip() not in removable)
        # Markdown lines may be escaped or formatted, so compare their visible text.
        def keep_md(line: str) -> bool:
            visible = re.sub(r"^#{1,6}\s+|^[-*>]\s+", "", line).replace("\\", "").strip()
            return visible not in removable
        page.markdown = "\n".join(line for line in md_lines if keep_md(line)).strip()

class PDFConverter:
    def __init__(self, source: Path, options: Options):
        self.source = source
        self.options = options
        self.warnings: list[str] = []
        self.metadata: dict[str, Any] = {}
        self.total_pages = 0
        self.selected_pages: list[int] = []
        self.assets_written: dict[str, str] = {}
        self.used_asset_names: set[str] = set()
        self.engine_used = ""

    def warn(self, message: str) -> None:
        if message not in self.warnings:
            self.warnings.append(message)

    def choose_engine(self) -> str:
        available = {
            "pymupdf": optional_import("pymupdf", "fitz") is not None,
            "pypdf": optional_import("pypdf") is not None,
            "pdftotext": executable("pdftotext") is not None,
        }
        if self.options.engine != "auto":
            if not available[self.options.engine]:
                instructions = {
                    "pymupdf": "instale PyMuPDF con: python -m pip install pymupdf",
                    "pypdf": "instale pypdf con: python -m pip install pypdf",
                    "pdftotext": "instale poppler-utils (debe incluir pdftotext)",
                }
                raise ConversionError(f"El motor {self.options.engine} no está disponible; {instructions[self.options.engine]}")
            return self.options.engine
        for engine in ("pymupdf", "pypdf", "pdftotext"):
            if available[engine]:
                return engine
        raise ConversionError(
            "No hay ningún motor PDF disponible. Instale el recomendado con: "
            "python -m pip install pymupdf"
        )

    def emit_image(self, data: bytes, extension: str, page_number: int, index: int) -> str:
        digest = hashlib.sha256(data).hexdigest()
        if digest in self.assets_written:
            return self.assets_written[digest]
        extension = re.sub(r"[^a-zA-Z0-9]", "", extension.lower()) or "bin"
        mime = {
            "jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
            "gif": "image/gif", "webp": "image/webp", "tif": "image/tiff",
            "tiff": "image/tiff", "jp2": "image/jp2", "jpx": "image/jpx",
        }.get(extension, f"image/{extension}")
        if self.options.images == "embed":
            uri = f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"
            self.assets_written[digest] = uri
            return uri
        stem = f"pagina-{page_number:04d}-imagen-{index:03d}"
        name = f"{stem}.{extension}"
        suffix = 2
        while name.casefold() in self.used_asset_names:
            name = f"{stem}-{suffix}.{extension}"
            suffix += 1
        self.used_asset_names.add(name.casefold())
        self.options.assets_dir.mkdir(parents=True, exist_ok=True)
        target = self.options.assets_dir / name
        write_bytes_atomic(target, data)
        relative = os.path.relpath(target, self.options.output.parent).replace(os.sep, "/")
        uri = urllib.parse.quote(relative, safe="/._-~")
        self.assets_written[digest] = uri
        return uri

    def should_ocr(self, text: str) -> bool:
        if self.options.ocr == "never":
            return False
        if self.options.ocr == "always":
            return True
        useful = sum(char.isalnum() for char in text)
        return useful < self.options.ocr_min_chars

    def render_page_for_ocr(self, page_index: int, fitz_page: Any | None = None) -> Path:
        handle, temporary = tempfile.mkstemp(prefix=f"pdf-ocr-{page_index + 1}-", suffix=".png")
        os.close(handle)
        target = Path(temporary)
        try:
            if fitz_page is not None:
                scale = self.options.ocr_dpi / 72.0
                module = optional_import("pymupdf", "fitz")
                matrix = module.Matrix(scale, scale)
                pixmap = fitz_page.get_pixmap(matrix=matrix, alpha=False)
                pixmap.save(str(target))
                return target
            if executable("mutool"):
                command = ["mutool", "draw", "-q", "-F", "png", "-r", str(self.options.ocr_dpi)]
                if self.options.password:
                    command.extend(["-p", self.options.password])
                command.extend(["-o", str(target), str(self.source), str(page_index + 1)])
            elif executable("pdftoppm"):
                target.unlink(missing_ok=True)
                prefix = str(target.with_suffix(""))
                command = ["pdftoppm", "-f", str(page_index + 1), "-l", str(page_index + 1),
                           "-singlefile", "-r", str(self.options.ocr_dpi), "-png"]
                if self.options.password:
                    command.extend(["-upw", self.options.password])
                command.extend([str(self.source), prefix])
            else:
                raise ConversionError("El OCR necesita PyMuPDF, mutool o pdftoppm para renderizar las páginas")
            run_command(command, self.options.timeout)
            if not target.is_file() or target.stat().st_size == 0:
                raise ConversionError(f"No se pudo renderizar la página {page_index + 1} para OCR")
            return target
        except BaseException:
            target.unlink(missing_ok=True)
            raise

    def ocr_page(self, page_index: int, fitz_page: Any | None = None) -> str:
        if not executable("tesseract"):
            raise ConversionError(
                "Se solicitó OCR pero Tesseract no está instalado. Instale tesseract-ocr "
                "y el paquete de idioma correspondiente, o use --ocr never."
            )
        image = self.render_page_for_ocr(page_index, fitz_page)
        try:
            command = ["tesseract", str(image), "stdout", "-l", self.options.ocr_language,
                       "--psm", str(self.options.ocr_psm), "quiet"]
            completed = run_command(command, self.options.timeout)
            return clean_text(completed.stdout)
        finally:
            image.unlink(missing_ok=True)

    def extract_with_pymupdf(self) -> list[PageResult]:
        fitz = optional_import("pymupdf", "fitz")
        assert fitz is not None
        try:
            document = fitz.open(str(self.source))
        except Exception as exc:
            raise ConversionError(f"No se pudo abrir el PDF con PyMuPDF: {exc}") from exc
        with document:
            if getattr(document, "needs_pass", False):
                if not self.options.password or not document.authenticate(self.options.password):
                    raise ConversionError("El PDF está cifrado; proporcione la contraseña correcta con --password")
            self.total_pages = len(document)
            self.validate_page_count()
            self.selected_pages = parse_page_spec(self.options.pages, self.total_pages)
            self.metadata = {key: value for key, value in (document.metadata or {}).items() if value}

            page_dicts: dict[int, dict[str, Any]] = {}
            weighted_sizes: list[float] = []
            for index in self.selected_pages:
                data = document[index].get_text("dict", sort=False)
                page_dicts[index] = data
                for block in data.get("blocks", []):
                    if block.get("type", 0) != 0:
                        continue
                    for line in block.get("lines", []):
                        for span in line.get("spans", []):
                            text = span.get("text", "").strip()
                            size = float(span.get("size", 0))
                            weighted_sizes.extend([size] * min(50, max(1, len(text))))
            body_size = statistics.median(weighted_sizes) if weighted_sizes else 11.0
            return [self.pymupdf_page(document[index], page_dicts[index], body_size) for index in self.selected_pages]

    def pymupdf_page(self, page: Any, data: dict[str, Any], body_size: float) -> PageResult:
        page_number = int(page.number) + 1
        elements: list[Element] = []
        raw_lines: list[str] = []
        table_boxes: list[tuple[float, float, float, float]] = []
        if self.options.tables and hasattr(page, "find_tables"):
            try:
                found = page.find_tables()
                for table in getattr(found, "tables", []):
                    rendered = table_to_markdown(table.extract())
                    if rendered:
                        bbox = tuple(float(value) for value in table.bbox)
                        table_boxes.append(bbox)  # type: ignore[arg-type]
                        elements.append(Element(bbox[1], bbox[0], "table", rendered, bbox))
            except Exception as exc:
                self.warn(f"Página {page_number}: no se pudieron reconstruir las tablas ({exc})")

        links: list[tuple[tuple[float, float, float, float], str]] = []
        try:
            for link in page.get_links():
                uri = str(link.get("uri", "")).strip()
                rect = link.get("from")
                if uri and rect:
                    links.append((tuple(float(value) for value in rect), uri))
        except Exception as exc:
            self.warn(f"Página {page_number}: no se pudieron leer los enlaces ({exc})")

        image_index = 0
        for block in data.get("blocks", []):
            bbox = tuple(float(value) for value in block.get("bbox", (0, 0, 0, 0)))
            if block.get("type", 0) == 1:
                if self.options.images == "ignore":
                    continue
                width, height = int(block.get("width", 0)), int(block.get("height", 0))
                image = block.get("image")
                if not image or width < self.options.min_image_width or height < self.options.min_image_height:
                    continue
                image_index += 1
                extension = str(block.get("ext", "png"))
                uri = self.emit_image(bytes(image), extension, page_number, image_index)
                elements.append(Element(bbox[1], bbox[0], "image", f"![Imagen de la página {page_number}]({markdown_url(uri)})", bbox))
                continue
            if block.get("type", 0) != 0:
                continue
            if any(rectangle_intersection_ratio(bbox, table_box) > 0.6 for table_box in table_boxes):
                continue
            block_lines: list[str] = []
            heading_levels: list[int | None] = []
            for line in block.get("lines", []):
                line_bbox = tuple(float(value) for value in line.get("bbox", bbox))
                if any(rectangle_intersection_ratio(line_bbox, table_box) > 0.6 for table_box in table_boxes):
                    continue
                rendered_spans: list[str] = []
                raw_spans: list[str] = []
                max_size = 0.0
                for span in line.get("spans", []):
                    raw = clean_inline_text(str(span.get("text", "")))
                    core = raw.strip()
                    if not core:
                        continue
                    raw_spans.append(raw)
                    max_size = max(max_size, float(span.get("size", body_size)))
                    rendered = markdown_escape(core)
                    flags = int(span.get("flags", 0))
                    font = str(span.get("font", "")).casefold()
                    is_mono = bool(flags & 8) or any(name in font for name in ("courier", "mono", "consolas"))
                    is_bold = bool(flags & 16) or any(name in font for name in ("bold", "black", "heavy", "semibold"))
                    is_italic = bool(flags & 2) or any(name in font for name in ("italic", "oblique"))
                    if is_mono and "`" not in rendered:
                        rendered = f"`{rendered}`"
                    else:
                        if is_bold:
                            rendered = f"**{rendered}**"
                        if is_italic:
                            rendered = f"*{rendered}*"
                    span_bbox = tuple(float(value) for value in span.get("bbox", line_bbox))
                    for link_bbox, uri in links:
                        if rectangle_intersection_ratio(span_bbox, link_bbox) > 0.35:
                            rendered = f"[{rendered}]({markdown_url(uri)})"
                            break
                    rendered_spans.append(
                        (" " if raw.startswith(" ") else "")
                        + rendered
                        + (" " if raw.endswith(" ") else "")
                    )
                raw_line = "".join(raw_spans).strip()
                rendered_line = "".join(rendered_spans).strip()
                if not raw_line:
                    continue
                raw_lines.append(raw_line)
                rendered_line = re.sub(r"^[•◦▪‣]\s*", "- ", rendered_line)
                block_lines.append(rendered_line)
                ratio = max_size / max(body_size, 1.0)
                level = None
                if len(raw_line) <= 180 and not LIST_RE.match(raw_line) and ratio >= 1.18:
                    level = 1 if ratio >= 1.9 else 2 if ratio >= 1.55 else 3 if ratio >= 1.32 else 4
                heading_levels.append(level)
            if not block_lines:
                continue
            if len(block_lines) == 1 and heading_levels[0]:
                content = "#" * int(heading_levels[0]) + " " + block_lines[0]
            elif self.options.preserve_line_breaks:
                content = "  \n".join(block_lines)
            else:
                content = join_wrapped_lines(block_lines, self.options.dehyphenate)
            if content:
                elements.append(Element(bbox[1], bbox[0], "text", content, bbox))

        elements = self.sort_layout_elements(elements, float(page.rect.width))
        markdown = "\n\n".join(element.content for element in elements if element.content).strip()
        raw_text = "\n".join(raw_lines)
        if self.should_ocr(raw_text):
            try:
                recognized = self.ocr_page(page.number, page)
                if recognized:
                    raw_text = recognized
                    recognized_markdown = plain_text_to_markdown(recognized, self.options)
                    extras = "\n\n".join(
                        element.content for element in elements
                        if element.kind in {"table", "image"} and element.content
                    )
                    markdown = "\n\n".join(part for part in (recognized_markdown, extras) if part)
            except ConversionError as exc:
                if self.options.ocr == "always" or self.options.strict:
                    raise
                self.warn(f"Página {page_number}: OCR omitido ({exc})")
        return PageResult(page_number, markdown, raw_text)

    @staticmethod
    def sort_layout_elements(elements: list[Element], page_width: float) -> list[Element]:
        """Apply a modest two-column reading-order heuristic."""
        if len(elements) < 4:
            return sorted(elements, key=lambda item: (round(item.y, 1), item.x))
        midpoint = page_width / 2
        left = [item for item in elements if item.bbox and item.bbox[2] <= midpoint * 1.12]
        right = [item for item in elements if item.bbox and item.bbox[0] >= midpoint * 0.88]
        wide = [item for item in elements if item.bbox and item.bbox[0] < midpoint * 0.75 and item.bbox[2] > midpoint * 1.25]
        if len(left) >= 2 and len(right) >= 2 and len(wide) <= max(1, len(elements) // 4):
            columns = sorted(left, key=lambda item: (item.y, item.x)) + sorted(right, key=lambda item: (item.y, item.x))
            column_ids = {id(item) for item in left + right}
            non_columns = sorted((item for item in elements if id(item) not in column_ids), key=lambda item: (item.y, item.x))
            # Full-width titles above both columns remain first.
            if columns:
                first_column_y = min(item.y for item in columns)
                before = [item for item in non_columns if item.y < first_column_y]
                after = [item for item in non_columns if item.y >= first_column_y]
                return before + columns + after
        return sorted(elements, key=lambda item: (round(item.y, 1), item.x))

    def open_pypdf(self) -> tuple[Any, Any]:
        pypdf = optional_import("pypdf")
        assert pypdf is not None
        try:
            reader = pypdf.PdfReader(str(self.source))
            if reader.is_encrypted:
                result = reader.decrypt(self.options.password)
                if not result:
                    raise ConversionError("El PDF está cifrado; proporcione la contraseña correcta con --password")
            return pypdf, reader
        except ConversionError:
            raise
        except Exception as exc:
            raise ConversionError(f"No se pudo abrir el PDF con pypdf: {exc}") from exc

    def extract_with_pypdf(self) -> list[PageResult]:
        _, reader = self.open_pypdf()
        self.total_pages = len(reader.pages)
        self.validate_page_count()
        self.selected_pages = parse_page_spec(self.options.pages, self.total_pages)
        raw_metadata = reader.metadata or {}
        self.metadata = {str(key).lstrip("/"): str(value) for key, value in raw_metadata.items() if value}
        pages: list[PageResult] = []
        for index in self.selected_pages:
            page = reader.pages[index]
            try:
                try:
                    raw = page.extract_text(extraction_mode="layout") or ""
                except (TypeError, ValueError):
                    raw = page.extract_text() or ""
            except Exception as exc:
                raw = ""
                self.warn(f"Página {index + 1}: pypdf no pudo extraer el texto ({exc})")
            markdown = plain_text_to_markdown(raw, self.options)
            link_lines: list[str] = []
            rendered_links = ""
            try:
                annotations = page.get("/Annots") or []
                for reference in annotations:
                    annotation = reference.get_object()
                    action = annotation.get("/A") or {}
                    uri = str(action.get("/URI", "")).strip()
                    if URI_RE.match(uri) and uri not in link_lines:
                        link_lines.append(uri)
            except Exception as exc:
                self.warn(f"Página {index + 1}: no se pudieron leer los enlaces ({exc})")
            if link_lines:
                rendered_links = "\n".join(f"- [{markdown_escape(uri)}]({markdown_url(uri)})" for uri in link_lines)
                markdown = (markdown + "\n\nEnlaces:\n\n" + rendered_links).strip()
            image_lines: list[str] = []
            if self.options.images != "ignore":
                try:
                    for image_index, image in enumerate(page.images, 1):
                        data = bytes(image.data)
                        name = str(image.name)
                        extension = Path(name).suffix.lstrip(".") or "png"
                        try:
                            width, height = image.image.size
                        except Exception:
                            width = height = max(self.options.min_image_width, self.options.min_image_height)
                        if width < self.options.min_image_width or height < self.options.min_image_height:
                            continue
                        uri = self.emit_image(data, extension, index + 1, image_index)
                        image_lines.append(f"![Imagen de la página {index + 1}]({markdown_url(uri)})")
                    if image_lines:
                        markdown = (markdown + "\n\n" + "\n\n".join(image_lines)).strip()
                except Exception as exc:
                    self.warn(f"Página {index + 1}: no se pudieron extraer las imágenes ({exc})")
            if self.should_ocr(raw):
                try:
                    recognized = self.ocr_page(index)
                    if recognized:
                        raw = recognized
                        markdown = plain_text_to_markdown(recognized, self.options)
                        if rendered_links:
                            markdown += "\n\nEnlaces:\n\n" + rendered_links
                        if image_lines:
                            markdown += "\n\n" + "\n\n".join(image_lines)
                except ConversionError as exc:
                    if self.options.ocr == "always" or self.options.strict:
                        raise
                    self.warn(f"Página {index + 1}: OCR omitido ({exc})")
            pages.append(PageResult(index + 1, markdown, clean_text(raw)))
        if self.options.tables:
            self.warn("El motor pypdf no reconstruye tablas; use --engine pymupdf para esa función")
        return pages

    def pdfinfo(self) -> tuple[int, dict[str, str]]:
        if not executable("pdfinfo"):
            raise ConversionError("pdftotext requiere pdfinfo para seleccionar y validar las páginas")
        command = ["pdfinfo"]
        if self.options.password:
            command.extend(["-upw", self.options.password])
        command.append(str(self.source))
        completed = run_command(command, self.options.timeout)
        values: dict[str, str] = {}
        for line in completed.stdout.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                values[key.strip()] = value.strip()
        try:
            return int(values["Pages"]), values
        except (KeyError, ValueError) as exc:
            raise ConversionError("pdfinfo no devolvió el número de páginas") from exc

    def extract_with_pdftotext(self) -> list[PageResult]:
        self.total_pages, info = self.pdfinfo()
        self.validate_page_count()
        self.selected_pages = parse_page_spec(self.options.pages, self.total_pages)
        self.metadata = {key.casefold(): value for key, value in info.items() if key in {"Title", "Author", "Subject", "Keywords", "Creator", "Producer", "CreationDate", "ModDate"}}
        pages: list[PageResult] = []
        for index in self.selected_pages:
            command = ["pdftotext", "-enc", "UTF-8", "-f", str(index + 1), "-l", str(index + 1)]
            command.append("-layout" if self.options.preserve_line_breaks else "-raw")
            if self.options.password:
                command.extend(["-upw", self.options.password])
            command.extend([str(self.source), "-"])
            completed = run_command(command, self.options.timeout)
            raw = clean_text(completed.stdout.replace("\f", ""))
            markdown = plain_text_to_markdown(raw, self.options)
            if self.should_ocr(raw):
                try:
                    recognized = self.ocr_page(index)
                    if recognized:
                        raw = recognized
                        markdown = plain_text_to_markdown(recognized, self.options)
                except ConversionError as exc:
                    if self.options.ocr == "always" or self.options.strict:
                        raise
                    self.warn(f"Página {index + 1}: OCR omitido ({exc})")
            pages.append(PageResult(index + 1, markdown, raw))
        if self.options.images != "ignore":
            self.warn("El motor pdftotext no extrae imágenes; use --engine pymupdf")
        if self.options.tables:
            self.warn("El motor pdftotext no reconstruye tablas; use --engine pymupdf")
        return pages

    def validate_page_count(self) -> None:
        if self.total_pages < 1:
            raise ConversionError("El PDF no contiene páginas")
        if self.total_pages > self.options.max_pages:
            raise ConversionError(
                f"El PDF tiene {self.total_pages} páginas y supera el límite de seguridad "
                f"de {self.options.max_pages}; cambie --max-pages para continuar"
            )

    def front_matter(self) -> str:
        preferred = {
            "title": ("title", "Title"), "author": ("author", "Author"),
            "subject": ("subject", "Subject"), "keywords": ("keywords", "Keywords"),
            "creator": ("creator", "Creator"), "producer": ("producer", "Producer"),
            "creation_date": ("creationDate", "CreationDate", "creationdate"),
            "modified_date": ("modDate", "ModDate", "moddate"),
        }
        lines = ["---"]
        for output_key, source_keys in preferred.items():
            value = next((self.metadata[key] for key in source_keys if self.metadata.get(key)), None)
            if value is not None:
                lines.append(f"{output_key}: {yaml_string(value)}")
        lines.extend([
            f"source: {yaml_string(self.source.name)}",
            f"pages: {len(self.selected_pages)}",
            f"pdf_engine: {yaml_string(self.engine_used)}",
            "---",
        ])
        return "\n".join(lines)

    @staticmethod
    def make_toc(markdown: str) -> str:
        entries: list[tuple[int, str, str]] = []
        seen: Counter[str] = Counter()
        for line in markdown.splitlines():
            match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
            if not match:
                continue
            level = len(match.group(1))
            label = re.sub(r"[*_`\[\]<>]", "", match.group(2)).strip()
            anchor = unicodedata.normalize("NFKD", label).encode("ascii", "ignore").decode().casefold()
            anchor = re.sub(r"[^a-z0-9 _-]", "", anchor).replace(" ", "-")
            anchor = re.sub(r"-+", "-", anchor).strip("-") or "seccion"
            count = seen[anchor]
            seen[anchor] += 1
            if count:
                anchor += f"-{count}"
            entries.append((level, label, anchor))
        if not entries:
            return ""
        minimum = min(level for level, _, _ in entries)
        return "\n".join("  " * (level - minimum) + f"- [{label}](#{anchor})" for level, label, anchor in entries)

    def convert(self) -> tuple[str, list[str]]:
        self.engine_used = self.choose_engine()
        if self.engine_used == "pymupdf":
            pages = self.extract_with_pymupdf()
        elif self.engine_used == "pypdf":
            pages = self.extract_with_pypdf()
        else:
            pages = self.extract_with_pdftotext()
        if not self.options.keep_headers_footers:
            remove_repeated_headers_footers(pages)
        chunks: list[str] = []
        if self.options.front_matter:
            chunks.append(self.front_matter())
        body_chunks: list[str] = []
        for page in pages:
            marker = ""
            if self.options.page_markers == "comment":
                marker = f"<!-- page: {page.number} -->"
            elif self.options.page_markers == "heading":
                marker = f"## Página {page.number}"
            content = page.markdown.strip()
            if marker or content:
                body_chunks.append("\n\n".join(part for part in (marker, content) if part))
        body = "\n\n".join(body_chunks)
        if self.options.toc:
            toc = self.make_toc(body)
            if toc:
                chunks.append("## Índice\n\n" + toc)
            else:
                self.warn("No se encontraron encabezados para crear el índice")
        if body:
            chunks.append(body)
        markdown = "\n\n".join(chunks)
        markdown = re.sub(r"[ \t]+\n", "\n", markdown)
        markdown = re.sub(r"\n{3,}", "\n\n", markdown).rstrip() + "\n"
        return markdown, self.warnings

def run_command(command: list[str], timeout: int) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, encoding="utf-8", errors="replace", timeout=timeout,
        )
    except FileNotFoundError as exc:
        raise ConversionError(f"No se encontró el programa externo: {command[0]}") from exc
    except subprocess.TimeoutExpired as exc:
        raise ConversionError(f"El proceso {command[0]} superó el límite de {timeout} segundos") from exc
    except subprocess.CalledProcessError as exc:
        detail = clean_text(exc.stderr) or clean_text(exc.stdout) or f"código {exc.returncode}"
        raise ConversionError(f"Falló {command[0]}: {detail}") from exc

def write_bytes_atomic(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(content)
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise

def write_text_atomic(path: Path, content: str) -> None:
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

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convierte un PDF digital o escaneado a Markdown.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
            Ejemplos:
              %(prog)s informe.pdf
              %(prog)s informe.pdf -o README.md --front-matter --toc
              %(prog)s libro.pdf --pages 1-10,15 --images copy
              %(prog)s escaneado.pdf --ocr always --ocr-language spa
              %(prog)s privado.pdf --password 'secreto' --overwrite

            Motores (en orden automático):
              pymupdf   Recomendado: diseño, estilos, tablas, enlaces e imágenes.
              pypdf     Texto, metadatos, enlaces e imágenes; sin tablas.
              pdftotext Alternativa de Poppler centrada en texto.

            Dependencias recomendadas:
              python -m pip install pymupdf
              Para OCR: tesseract-ocr y el paquete del idioma deseado.

            Nota: PDF describe posiciones, no la estructura lógica original. La
            lectura en documentos con maquetación compleja siempre es aproximada.
        """),
    )
    parser.add_argument("input", type=Path, help="archivo PDF de entrada")
    parser.add_argument("-o", "--output", type=Path, help="salida Markdown (por defecto: mismo nombre con .md)")
    parser.add_argument("--engine", choices=("auto", "pymupdf", "pypdf", "pdftotext"), default="auto",
                        help="motor de extracción (por defecto: auto)")
    parser.add_argument("--pages", default="all", metavar="RANGO",
                        help="páginas: all, 1-5, 1,3,8- o -10 (por defecto: all)")
    parser.add_argument("--password", default="", help="contraseña del PDF cifrado")
    parser.add_argument("--assets-dir", type=Path, help="carpeta de imágenes (por defecto: <salida>_assets)")
    parser.add_argument("--images", choices=("copy", "embed", "ignore"), default="copy",
                        help="copiar, incrustar u omitir imágenes (por defecto: copy)")
    parser.add_argument("--tables", action=argparse.BooleanOptionalAction, default=True,
                        help="reconstruir tablas cuando el motor lo permita (por defecto: sí)")
    parser.add_argument("--ocr", choices=("auto", "always", "never"), default="auto",
                        help="OCR en páginas sin texto, todas o ninguna (por defecto: auto)")
    parser.add_argument("--ocr-language", default="spa+eng", metavar="IDIOMAS",
                        help="idiomas Tesseract, p. ej. spa o spa+eng (por defecto: spa+eng)")
    parser.add_argument("--ocr-dpi", type=int, default=300, metavar="DPI", help="resolución del OCR (por defecto: 300)")
    parser.add_argument("--ocr-psm", type=int, choices=range(0, 14), default=1, metavar="0-13",
                        help="modo de segmentación Tesseract (por defecto: 1)")
    parser.add_argument("--ocr-min-chars", type=int, default=40, metavar="N",
                        help="caracteres alfanuméricos mínimos antes de OCR automático (por defecto: 40)")
    parser.add_argument("--page-markers", choices=("comment", "heading", "none"), default="comment",
                        help="separación entre páginas (por defecto: comment)")
    parser.add_argument("--front-matter", action="store_true", help="añadir metadatos como front matter YAML")
    parser.add_argument("--toc", action="store_true", help="crear un índice desde los encabezados detectados")
    parser.add_argument("--preserve-line-breaks", action="store_true", help="conservar los saltos visuales del PDF")
    parser.add_argument("--keep-headers-footers", action="store_true", help="no eliminar encabezados, pies y números repetidos")
    parser.add_argument("--no-dehyphenate", dest="dehyphenate", action="store_false",
                        help="no unir palabras separadas con guion al final de línea")
    parser.add_argument("--min-image-width", type=int, default=80, metavar="PX",
                        help="ancho mínimo para extraer una imagen (por defecto: 80)")
    parser.add_argument("--min-image-height", type=int, default=80, metavar="PX",
                        help="alto mínimo para extraer una imagen (por defecto: 80)")
    parser.add_argument("--max-file-mb", type=int, default=1024, metavar="MB",
                        help="tamaño máximo de entrada (por defecto: 1024)")
    parser.add_argument("--max-pages", type=int, default=5000, metavar="N",
                        help="máximo de páginas permitido (por defecto: 5000)")
    parser.add_argument("--timeout", type=int, default=120, metavar="SEGUNDOS",
                        help="límite por proceso OCR/PDF externo (por defecto: 120)")
    parser.add_argument("--overwrite", action="store_true", help="sobrescribir una salida existente")
    parser.add_argument("--strict", action="store_true", help="tratar cualquier advertencia como error")
    parser.add_argument("--quiet", action="store_true", help="no mostrar mensajes informativos")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return parser

def positive(parser: argparse.ArgumentParser, name: str, value: int, minimum: int = 1) -> None:
    if value < minimum:
        parser.error(f"{name} debe ser mayor o igual que {minimum}")

def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    source = args.input.expanduser().resolve()
    if not source.is_file():
        parser.error(f"no existe el archivo de entrada: {source}")
    if source.suffix.casefold() != ".pdf":
        parser.error("el archivo de entrada debe tener extensión .pdf")
    positive(parser, "--max-file-mb", args.max_file_mb)
    positive(parser, "--max-pages", args.max_pages)
    positive(parser, "--timeout", args.timeout)
    positive(parser, "--ocr-dpi", args.ocr_dpi, 72)
    positive(parser, "--ocr-min-chars", args.ocr_min_chars, 0)
    positive(parser, "--min-image-width", args.min_image_width, 0)
    positive(parser, "--min-image-height", args.min_image_height, 0)
    if source.stat().st_size > args.max_file_mb * 1024 * 1024:
        parser.error(f"el PDF supera el límite de {args.max_file_mb} MiB; cambie --max-file-mb")
    output = (args.output or source.with_suffix(".md")).expanduser().resolve()
    if output == source:
        parser.error("la salida no puede ser el mismo archivo que la entrada")
    if output.exists() and not args.overwrite:
        parser.error(f"la salida ya existe: {output} (use --overwrite)")
    assets_dir = (args.assets_dir or output.parent / f"{output.stem}_assets").expanduser().resolve()
    options = Options(
        output=output, assets_dir=assets_dir, engine=args.engine, pages=args.pages,
        password=args.password, images=args.images, tables=args.tables, ocr=args.ocr,
        ocr_language=args.ocr_language, ocr_dpi=args.ocr_dpi, ocr_psm=args.ocr_psm,
        ocr_min_chars=args.ocr_min_chars, page_markers=args.page_markers,
        front_matter=args.front_matter, toc=args.toc,
        preserve_line_breaks=args.preserve_line_breaks,
        keep_headers_footers=args.keep_headers_footers, dehyphenate=args.dehyphenate,
        min_image_width=args.min_image_width, min_image_height=args.min_image_height,
        max_file_mb=args.max_file_mb, max_pages=args.max_pages, timeout=args.timeout,
        overwrite=args.overwrite, strict=args.strict, quiet=args.quiet,
    )
    converter = PDFConverter(source, options)
    try:
        markdown, warnings = converter.convert()
        if args.strict and warnings:
            raise ConversionError("Conversión detenida por --strict:\n- " + "\n- ".join(warnings))
        write_text_atomic(output, markdown)
    except (ConversionError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    if not args.quiet:
        print(f"Creado: {output}", file=sys.stderr)
        print(f"Motor: {converter.engine_used}; páginas: {len(converter.selected_pages)}/{converter.total_pages}", file=sys.stderr)
        if args.images == "copy" and converter.assets_written:
            print(f"Recursos: {assets_dir} ({len(converter.assets_written)} imágenes)", file=sys.stderr)
        for warning in warnings:
            print(f"Advertencia: {warning}", file=sys.stderr)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
