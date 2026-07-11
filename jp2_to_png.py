#!/usr/bin/env python3
"""Convierte imágenes JPEG 2000 (JP2) de una carpeta a PNG.

Requiere Pillow con soporte para JPEG 2000. Instálalo con:
    python -m pip install Pillow
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, UnidentifiedImageError
except ImportError:  # Se informa en main para que --help siga funcionando.
    Image = None  # type: ignore[assignment,misc]
    UnidentifiedImageError = OSError

JP2_EXTENSIONS = {".jp2", ".j2k", ".jpf", ".jpx", ".jpc"}

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convierte recursivamente imágenes JP2 de una carpeta a PNG.",
        epilog="Ejemplo: python jp2_to_png.py /ruta/a/imagenes",
    )
    parser.add_argument("folder", type=Path, help="carpeta que contiene las imágenes JP2")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        help="carpeta de salida (por defecto: <carpeta>_png)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="permite reutilizar la carpeta de salida y sobrescribir PNG existentes",
    )
    return parser

def output_for(source: Path, source_root: Path, output_root: Path) -> Path:
    """Obtiene la ruta PNG conservando la estructura de subcarpetas."""
    return output_root / source.relative_to(source_root).with_suffix(".png")

def find_images(source_root: Path) -> list[Path]:
    return sorted(
        path
        for path in source_root.rglob("*")
        if path.is_file() and path.suffix.casefold() in JP2_EXTENSIONS
    )

def validate_destinations(images: list[Path], source_root: Path, output_root: Path) -> None:
    destinations: dict[Path, Path] = {}
    for image in images:
        destination = output_for(image, source_root, output_root)
        other = destinations.get(destination)
        if other is not None:
            raise ValueError(
                "colisión de nombres: "
                f"{other.relative_to(source_root)} y {image.relative_to(source_root)} "
                f"producirían {destination.relative_to(output_root)}"
            )
        destinations[destination] = image

def convert_image(source: Path, destination: Path) -> None:
    assert Image is not None
    destination.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        image.load()
        # PNG no admite CMYK; convertirlo evita un error al guardar.
        if image.mode == "CMYK":
            image = image.convert("RGB")
        image.save(destination, format="PNG")

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if Image is None:
        print("Error: falta Pillow. Instálalo con: python -m pip install Pillow", file=sys.stderr)
        return 2

    source_root = args.folder.expanduser().resolve()
    if not source_root.is_dir():
        print(f"Error: no existe la carpeta de entrada: {source_root}", file=sys.stderr)
        return 2

    output_root = (
        args.output_dir.expanduser().resolve()
        if args.output_dir
        else source_root.parent / f"{source_root.name}_png"
    )
    if output_root == source_root or source_root in output_root.parents:
        print("Error: la carpeta de salida no puede estar dentro de la carpeta de entrada.", file=sys.stderr)
        return 2
    if output_root.exists() and not args.overwrite:
        print(
            f"Error: la carpeta de salida ya existe: {output_root}\n"
            "Usa --overwrite para reutilizarla.",
            file=sys.stderr,
        )
        return 2

    images = find_images(source_root)
    if not images:
        print("No se encontraron imágenes JP2 para convertir.")
        return 0

    try:
        validate_destinations(images, source_root, output_root)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    converted = 0
    failed = 0
    for source in images:
        destination = output_for(source, source_root, output_root)
        try:
            print(f"Convirtiendo: {source.relative_to(source_root)}")
            convert_image(source, destination)
            converted += 1
        except (OSError, UnidentifiedImageError) as exc:
            failed += 1
            print(f"Error al convertir {source.relative_to(source_root)}: {exc}", file=sys.stderr)

    print(f"Convertidas: {converted}; errores: {failed}; salida: {output_root}")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
