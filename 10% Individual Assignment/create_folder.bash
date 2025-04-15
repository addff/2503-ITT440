#!/bin/bash

# Pastikan file folder.txt wujud
if [ ! -f "folder.txt" ]; then
  echo "Error: File folder.txt tidak ditemukan."
  exit 1
fi

# Baca setiap baris dari file folder.txt
while IFS= read -r line; do
  # Buang whitespace di belakang nama folder
  cleaned_name=$(echo "$line" | sed 's/[[:space:]]*$//')

  # Buang simbol-simbol di belakang nama folder
  cleaned_name=$(echo "$cleaned_name" | sed 's/[^a-zA-Z0-9._-]*$//')

  # Pastikan nama folder tidak kosong setelah dibersihkan
  if [ -n "$cleaned_name" ]; then
    # Buat folder jika belum wujud
    if [ ! -d "$cleaned_name" ]; then
      mkdir "$cleaned_name"
      echo "Folder '$cleaned_name' telah dibuat."

      # Buat file README.md di dalam folder yang baru dibuat
      echo "# $cleaned_name" > "$cleaned_name/README.md"
      echo "File README.md telah dibuat di dalam '$cleaned_name'."
    else
      echo "Folder '$cleaned_name' sudah wujud."
    fi
  fi
done < "folder.txt"

echo "Selesai membuat folder dan file README.md."

exit 0
