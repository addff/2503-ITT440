#!/bin/bash

# Loop through each line in folder.txt
while IFS= read -r dir_name; do
    # Remove the carriage return character (if any)
    cleaned_dir_name=$(echo "$dir_name" | sed 's/\r//')

    # Create the directory
    mkdir -p "$cleaned_dir_name"
    
    # Create the README.md file inside the directory
    touch "$cleaned_dir_name/README.md"
    
    echo "Created directory $cleaned_dir_name with README.md"
done < folder.txt
