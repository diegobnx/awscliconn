#!/bin/bash
array=()
while IFS= read -r line; do
  array+=("\"$line\"")
done < <(cat ../.saml2aws | grep "aws_profile" | cut -d " " -f12-)

# Concatenar os elementos do array separados por vírgula e espaço
formatted_output=$(IFS=", "; echo "[${array[*]}]")
echo "$formatted_output"

# Concatenar os elementos do array separados por elemento em returns
for element in "${array[@]}"; do
  echo "$element"
done
