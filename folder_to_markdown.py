#!/usr/bin/env python3
"""Convierte recursivamente una carpeta a una copia preparada para Markdown.

Los documentos DOCX y PDF se convierten mediante los dos scripts del mismo
directorio. El resto de archivos se copian conservando sus metadatos.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

def normalized_filename(name: str) -> str:
    """Devuelve un nombre portable: minúsculas, sin tildes ni símbolos."""
    path = Path(name)
    stem = unicodedata.normalize("NFKD", path.stem)
    stem = "".join(char for char in stem if not unicodedata.combining(char))
    stem = stem.encode("ascii", "ignore").decode("ascii").lower()
    stem = "".join(char if char.isalnum() else "_" for char in stem)
    stem = "_".join(part for part in stem.split("_") if part) or "archivo"

    suffix = unicodedata.normalize("NFKD", path.suffix)
    suffix = "".join(char for char in suffix if not unicodedata.combining(char))
    suffix = suffix.encode("ascii", "ignore").decode("ascii").lower()
    suffix = "".join(char for char in suffix if char.isalnum())
    return f"{stem}.{suffix}" if suffix else stem

def destination_for(source: Path, source_root: Path, destination_root: Path) -> Path:
    relative = source.relative_to(source_root)
    if source.suffix.casefold() in {".docx", ".pdf"}:
        name = normalized_filename(source.with_suffix(".md").name)
    else:
        name = normalized_filename(source.name)
    return destination_root / relative.parent / name

def validate_destinations(files: list[Path], source_root: Path, destination_root: Path) -> None:
    """Detecta pérdidas de datos por nombres que se normalizarían igual."""
    occupied: dict[Path, Path] = {}
    source_directories = {destination_root / item.relative_to(source_root) for item in source_root.rglob("*") if item.is_dir()}

    for source in files:
        destination = destination_for(source, source_root, destination_root)
        other = occupied.get(destination)
        if other is not None:
            raise ValueError(
                f"colisión de nombres: {other.relative_to(source_root)} y "
                f"{source.relative_to(source_root)} producirían {destination.relative_to(destination_root)}"
            )
        if destination in source_directories:
            raise ValueError(
                f"colisión entre archivo y carpeta: {source.relative_to(source_root)} produciría "
                f"{destination.relative_to(destination_root)}"
            )
        if source.suffix.casefold() in {".docx", ".pdf"}:
            assets = destination.parent / f"{destination.stem}_assets"
            if assets in source_directories:
                raise ValueError(
                    f"la carpeta de recursos de {source.relative_to(source_root)} colisionaría con "
                    f"{assets.relative_to(destination_root)}"
                )
        occupied[destination] = source

def convert(source: Path, destination: Path, script: Path) -> None:
    assets_dir = destination.parent / f"{destination.stem}_assets"
    command = [sys.executable, str(script), str(source), "-o", str(destination), "--assets-dir", str(assets_dir)]
    result = subprocess.run(command, check=False)
    if result.returncode:
        raise RuntimeError(f"falló la conversión de {source} (código {result.returncode})")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convierte recursivamente DOCX y PDF de una carpeta a Markdown.",
        epilog="Ejemplo: python folder_to_markdown.py /ruta/a/documentos",
    )
    parser.add_argument("folder", type=Path, help="carpeta de entrada")
    return parser

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    source_root = args.folder.expanduser().resolve()
    if not source_root.is_dir():
        print(f"Error: no existe la carpeta de entrada: {source_root}", file=sys.stderr)
        return 2

    destination_root = source_root.parent / f"{source_root.name}_md"
    if destination_root.exists():
        print(f"Error: la carpeta de salida ya existe: {destination_root}", file=sys.stderr)
        return 2

    files = sorted(item for item in source_root.rglob("*") if item.is_file())
    try:
        validate_destinations(files, source_root, destination_root)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    script_directory = Path(__file__).resolve().parent
    converters = {
        ".docx": script_directory / "docx_to_markdown.py",
        ".pdf": script_directory / "pdf_to_markdown.py",
    }
    for extension, script in converters.items():
        if not script.is_file():
            print(f"Error: no se encuentra el conversor {script.name}", file=sys.stderr)
            return 2

    destination_root.mkdir()
    for directory in sorted((item for item in source_root.rglob("*") if item.is_dir())):
        (destination_root / directory.relative_to(source_root)).mkdir(exist_ok=True)

    try:
        for source in files:
            destination = destination_for(source, source_root, destination_root)
            destination.parent.mkdir(parents=True, exist_ok=True)
            converter = converters.get(source.suffix.casefold())
            if converter:
                print(f"Convirtiendo: {source.relative_to(source_root)}")
                convert(source, destination, converter)
            else:
                print(f"Copiando: {source.relative_to(source_root)}")
                shutil.copy2(source, destination)
    except (OSError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Carpeta creada: {destination_root}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
