#!/usr/bin/env python3
"""Limpia recursivamente archivos Markdown y anota sus imágenes locales.

Para cada archivo Markdown de la carpeta indicada, el script:

* elimina los asteriscos de los títulos ATX (``# Título``, ``## Título``, ...);
* elimina las líneas que contienen referencias a imágenes locales inexistentes;
* añade, debajo de cada imagen válida, el contenido del archivo ``.md`` que
  comparte su nombre, delimitado con comentarios de inicio y fin.

Las descripciones se actualizan en cada ejecución, por lo que el script se
puede ejecutar más de una vez sin duplicar bloques.
"""

from __future__ import annotations

import argparse
import os
import re
import stat
import sys
import tempfile
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

MARKDOWN_EXTENSIONS = {".md", ".markdown", ".mdown", ".mkdn", ".mkd"}

# Las imágenes generadas por los conversores de este proyecto usan esta forma.
# También admite destinos entre <...>, necesarios cuando la ruta contiene espacios.
IMAGE_PATTERN = re.compile(
    r"!\[[^\]\n]*\]\(\s*(?:<(?P<bracketed>[^>\n]+)>|(?P<plain>[^)\s]+))(?:\s+[^)]*)?\)"
)
HEADING_PATTERN = re.compile(r"^(?P<prefix>[ \t]{0,3}#{1,6})(?=[ \t]|$)(?P<text>.*)$")
FENCE_PATTERN = re.compile(r"^[ \t]{0,3}(?P<fence>`{3,}|~{3,})")
DESCRIPTION_START = "<!-- INICIO DESCRIPCIÓN DE LA IMAGEN:"
DESCRIPTION_END = "<!-- FIN DESCRIPCIÓN DE LA IMAGEN:"

@dataclass
class Changes:
    """Cambios aplicados a un archivo Markdown."""

    heading_asterisks_removed: int = 0
    missing_image_lines_removed: int = 0
    descriptions_added: int = 0
    descriptions_updated: int = 0
    descriptions_removed: int = 0

    @property
    def changed(self) -> bool:
        return any(
            (
                self.heading_asterisks_removed,
                self.missing_image_lines_removed,
                self.descriptions_added,
                self.descriptions_updated,
                self.descriptions_removed,
            )
        )

@dataclass
class TransformResult:
    content: str
    changes: Changes

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Limpia recursivamente archivos Markdown y añade descripciones de imágenes.",
        epilog=(
            "Ejemplo: python3 limpiar_markdown.py /ruta/a/la/carpeta\n\n"
            "Una imagen llamada grafico.png puede tener su descripción en grafico.md."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("folder", type=Path, help="carpeta que contiene los archivos Markdown")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="muestra los cambios que se harían, sin modificar archivos",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="muestra también los archivos que no requieren cambios",
    )
    return parser

def print_planned_actions(folder: Path, dry_run: bool) -> None:
    """Informa de las operaciones antes de leer o modificar archivos."""
    mode = "simulación: no se modificará ningún archivo" if dry_run else "se modificarán los archivos directamente"
    print(f"Carpeta de trabajo: {folder}")
    print(f"Modo: {mode}.")
    print("Acciones que se realizarán en todos los Markdown y sus subcarpetas:")
    print("  1. Eliminar los asteriscos (*) de los títulos #, ##, ###, etc.")
    print("  2. Eliminar las líneas con imágenes locales que no existan.")
    print("  3. Añadir, tras cada imagen válida, su descripción desde el .md homónimo.")
    print("     La descripción quedará entre marcadores de INICIO y FIN claramente identificados.")
    print()

def iter_markdown_files(folder: Path) -> list[Path]:
    """Devuelve Markdown de la carpeta, sin inspeccionar el directorio de Git."""
    files: list[Path] = []
    for current, directories, names in os.walk(folder):
        directories[:] = sorted(name for name in directories if name != ".git")
        current_path = Path(current)
        files.extend(
            current_path / name
            for name in sorted(names)
            if (current_path / name).suffix.casefold() in MARKDOWN_EXTENSIONS
        )
    return sorted(files)

def split_content(content: str) -> tuple[list[str], str, bool]:
    """Separa líneas conservando el estilo de salto y si había salto final."""
    newline = "\r\n" if "\r\n" in content else "\n"
    has_final_newline = content.endswith(("\n", "\r"))
    return content.splitlines(), newline, has_final_newline

def join_content(lines: Iterable[str], newline: str, has_final_newline: bool) -> str:
    content = newline.join(lines)
    if content and has_final_newline:
        content += newline
    return content

def image_targets(line: str) -> list[str]:
    """Extrae las rutas de imágenes de una línea Markdown."""
    return [match.group("bracketed") or match.group("plain") for match in IMAGE_PATTERN.finditer(line)]

def local_path_for_image(markdown_file: Path, target: str) -> Path | None:
    """Resuelve una referencia local; devuelve ``None`` para referencias remotas."""
    reference = unquote(target.strip())
    parsed = urlsplit(reference)
    if parsed.scheme and parsed.scheme.casefold() != "file":
        return None
    if parsed.netloc and parsed.scheme != "file":
        return None

    image_path = Path(parsed.path)
    if parsed.scheme == "file":
        return image_path
    return markdown_file.parent / image_path

def image_exists(markdown_file: Path, target: str) -> tuple[bool, Path | None]:
    """Indica si existe la imagen local o si la referencia no puede verificarse."""
    image_path = local_path_for_image(markdown_file, target)
    if image_path is None:
        # Una URL HTTP(S), data: u otra referencia remota no se elimina.
        return True, None
    return image_path.is_file(), image_path

def fence_state_after(line: str, active_fence: tuple[str, int] | None) -> tuple[str, int] | None:
    """Actualiza el estado de un bloque de código cercado."""
    match = FENCE_PATTERN.match(line)
    if not match:
        return active_fence

    fence = match.group("fence")
    if active_fence is None:
        return fence[0], len(fence)
    character, minimum_length = active_fence
    if fence[0] == character and len(fence) >= minimum_length:
        return None
    return active_fence

def clean_heading(line: str, changes: Changes) -> str:
    """Elimina asteriscos sólo de títulos ATX, sin tocar el resto del texto."""
    match = HEADING_PATTERN.match(line)
    if not match or "*" not in match.group("text"):
        return line
    text = match.group("text")
    changes.heading_asterisks_removed += text.count("*")
    return f"{match.group('prefix')}{text.replace('*', '')}"

def description_block_end(lines: list[str], start: int) -> tuple[int, bool]:
    """Localiza un bloque de descripción creado por este script tras una imagen."""
    index = start
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index >= len(lines) or not lines[index].startswith(DESCRIPTION_START):
        return start, False

    for end in range(index + 1, len(lines)):
        if lines[end].startswith(DESCRIPTION_END):
            return end + 1, True
    return start, False

def sanitize_description(content: str, description_file: Path) -> str:
    """Aplica la limpieza básica al texto que se va a insertar como descripción."""
    lines, newline, has_final_newline = split_content(content)
    result: list[str] = []
    active_fence: tuple[str, int] | None = None
    ignored_changes = Changes()

    for line in lines:
        if active_fence is None:
            targets = image_targets(line)
            if targets and any(not image_exists(description_file, target)[0] for target in targets):
                continue
            line = clean_heading(line, ignored_changes)
        result.append(line)
        active_fence = fence_state_after(line, active_fence)

    return join_content(result, newline, has_final_newline).strip()

def description_for(image_path: Path | None, cache: dict[Path, str]) -> str | None:
    """Obtiene la descripción .md homónima de una imagen local existente."""
    if image_path is None:
        return None
    description_file = image_path.with_suffix(".md")
    if not description_file.is_file():
        return None

    description_file = description_file.resolve()
    if description_file not in cache:
        cache[description_file] = sanitize_description(
            description_file.read_text(encoding="utf-8"), description_file
        )
    return cache[description_file] or None

def description_markers(target: str, description: str) -> list[str]:
    """Crea un bloque inequívocamente delimitado para una descripción."""
    return [
        f"<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: {target} -->",
        *description.splitlines(),
        f"<!-- FIN DESCRIPCIÓN DE LA IMAGEN: {target} -->",
    ]

def transform_markdown(markdown_file: Path, content: str, description_cache: dict[Path, str]) -> TransformResult:
    """Limpia un Markdown y añade o actualiza sus bloques de descripción."""
    lines, newline, has_final_newline = split_content(content)
    result: list[str] = []
    changes = Changes()
    active_fence: tuple[str, int] | None = None
    index = 0

    while index < len(lines):
        line = lines[index]
        if active_fence is not None:
            result.append(line)
            active_fence = fence_state_after(line, active_fence)
            index += 1
            continue

        targets = image_targets(line)
        if targets:
            valid_paths: list[Path | None] = []
            missing_image = False
            for target in targets:
                exists, image_path = image_exists(markdown_file, target)
                missing_image |= not exists
                valid_paths.append(image_path)

            block_end, has_existing_description = description_block_end(lines, index + 1)
            if missing_image:
                changes.missing_image_lines_removed += 1
                index = block_end if has_existing_description else index + 1
                continue

            result.append(clean_heading(line, changes))
            index = block_end if has_existing_description else index + 1

            descriptions = [
                (target, description_for(image_path, description_cache))
                for target, image_path in zip(targets, valid_paths, strict=True)
            ]
            descriptions = [(target, description) for target, description in descriptions if description]
            if descriptions:
                result.append("")
                for position, (target, description) in enumerate(descriptions):
                    if position:
                        result.append("")
                    result.extend(description_markers(target, description))
                if has_existing_description:
                    changes.descriptions_updated += len(descriptions)
                else:
                    changes.descriptions_added += len(descriptions)
            elif has_existing_description:
                changes.descriptions_removed += 1
            continue

        cleaned_line = clean_heading(line, changes)
        result.append(cleaned_line)
        active_fence = fence_state_after(cleaned_line, active_fence)
        index += 1

    return TransformResult(join_content(result, newline, has_final_newline), changes)

def write_text_atomic(destination: Path, content: str) -> None:
    """Escribe el archivo de forma atómica y conserva sus permisos actuales."""
    mode = stat.S_IMODE(destination.stat().st_mode)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{destination.name}.", dir=destination.parent, text=True)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as temporary:
            temporary.write(content)
        os.chmod(temporary_name, mode)
        os.replace(temporary_name, destination)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise

def describe_changes(changes: Changes) -> str:
    """Resume cambios de un archivo en una sola línea."""
    details: list[str] = []
    if changes.heading_asterisks_removed:
        details.append(f"{changes.heading_asterisks_removed} asterisco(s) en títulos")
    if changes.missing_image_lines_removed:
        details.append(f"{changes.missing_image_lines_removed} línea(s) de imagen eliminada(s)")
    if changes.descriptions_added:
        details.append(f"{changes.descriptions_added} descripción(es) añadida(s)")
    if changes.descriptions_updated:
        details.append(f"{changes.descriptions_updated} descripción(es) actualizada(s)")
    if changes.descriptions_removed:
        details.append(f"{changes.descriptions_removed} descripción(es) eliminada(s)")
    return "; ".join(details) or "sin cambios"

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    folder = args.folder.expanduser().resolve()
    if not folder.is_dir():
        print(f"Error: no existe la carpeta de entrada: {folder}", file=sys.stderr)
        return 2

    print_planned_actions(folder, args.dry_run)
    markdown_files = iter_markdown_files(folder)
    if not markdown_files:
        print("No se encontraron archivos Markdown.")
        return 0

    description_cache: dict[Path, str] = {}
    transformed: list[tuple[Path, str, TransformResult]] = []
    try:
        for markdown_file in markdown_files:
            source = markdown_file.read_text(encoding="utf-8")
            transformed.append((markdown_file, source, transform_markdown(markdown_file, source, description_cache)))
    except (OSError, UnicodeDecodeError) as exc:
        print(f"Error: no se pudo procesar un archivo: {exc}", file=sys.stderr)
        return 1

    changed_files = 0
    for markdown_file, source, result in transformed:
        if result.content != source:
            changed_files += 1
            if not args.dry_run:
                try:
                    write_text_atomic(markdown_file, result.content)
                except OSError as exc:
                    print(f"Error al guardar {markdown_file}: {exc}", file=sys.stderr)
                    return 1
            print(f"{'Se modificaría' if args.dry_run else 'Modificado'}: "
                  f"{markdown_file.relative_to(folder)} ({describe_changes(result.changes)})")
        elif args.verbose:
            print(f"Sin cambios: {markdown_file.relative_to(folder)}")

    verb = "se modificarían" if args.dry_run else "se han modificado"
    print(f"\nResumen: {changed_files} de {len(markdown_files)} archivo(s) {verb}.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
