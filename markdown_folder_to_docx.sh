#!/usr/bin/env bash
# Convierte recursivamente los archivos Markdown de una carpeta a DOCX usando
# pandoc. Crea una carpeta hermana con el sufijo _md_to_docx y conserva los
# demás archivos y subcarpetas.

set -euo pipefail

usage() {
  cat <<'EOF'
Uso: ./markdown_folder_to_docx.sh CARPETA_DE_ENTRADA

Convierte los archivos .md y .markdown (sin distinguir mayúsculas) a .docx
mediante pandoc. La salida se crea junto a la carpeta de entrada con el
sufijo _md_to_docx.

Ejemplo:
  ./markdown_folder_to_docx.sh /ruta/a/apuntes
  # Crea /ruta/a/apuntes_md_to_docx
EOF
}

is_markdown() {
  local path=${1,,}
  [[ "$path" == *.md || "$path" == *.markdown ]]
}

if [[ $# -ne 1 || "$1" == "-h" || "$1" == "--help" ]]; then
  usage
  [[ $# -eq 1 ]] && exit 0
  exit 2
fi

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc no está instalado o no está disponible en PATH." >&2
  exit 127
fi

input_dir=$1
if [[ ! -d "$input_dir" ]]; then
  echo "Error: la carpeta de entrada no existe: $input_dir" >&2
  exit 2
fi

input_dir=$(cd "$input_dir" && pwd -P)
parent_dir=$(dirname "$input_dir")
input_name=$(basename "$input_dir")
output_dir="$parent_dir/${input_name}_md_to_docx"

if [[ -e "$output_dir" ]]; then
  echo "Error: la carpeta de salida ya existe: $output_dir" >&2
  exit 2
fi

# Se comprueban las rutas resultantes antes de crear la salida, por ejemplo
# cuando documento.md y documento.docx coexistirían en el destino.
declare -A destinations=()
while IFS= read -r -d '' source_file; do
  relative_path=${source_file#"$input_dir"/}
  if is_markdown "$relative_path"; then
    destination_relative="${relative_path%.*}.docx"
  else
    destination_relative=$relative_path
  fi

  if [[ -v "destinations[$destination_relative]" ]]; then
    echo "Error: colisión de salida entre '${destinations[$destination_relative]}' y '$relative_path'." >&2
    exit 2
  fi
  destinations["$destination_relative"]=$relative_path
done < <(find "$input_dir" -type f -print0)

mkdir "$output_dir"

# Primero se reproducen las carpetas, incluidas las que estén vacías.
while IFS= read -r -d '' source_dir; do
  relative_path=${source_dir#"$input_dir"/}
  [[ "$source_dir" == "$input_dir" ]] && continue
  mkdir -p "$output_dir/$relative_path"
done < <(find "$input_dir" -type d -print0)

while IFS= read -r -d '' source_file; do
  relative_path=${source_file#"$input_dir"/}
  if is_markdown "$relative_path"; then
    destination_file="$output_dir/${relative_path%.*}.docx"
    mkdir -p "$(dirname "$destination_file")"
    echo "Convirtiendo: $relative_path"
    pandoc "$source_file" --table-of-contents --output="$destination_file"
  else
    destination_file="$output_dir/$relative_path"
    mkdir -p "$(dirname "$destination_file")"
    echo "Copiando: $relative_path"
    cp -p "$source_file" "$destination_file"
  fi
done < <(find "$input_dir" -type f -print0)

echo "Carpeta creada: $output_dir"
