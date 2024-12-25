#!/bin/bash

# Check if the filename is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <file_name>"
    exit 1
fi

# File containing the URLs
url_file="$1"

# Ensure the URL file exists
if [ ! -f "$url_file" ]; then
    echo "File $url_file does not exist."
    exit 1
fi

# Create a directory to store the responses
mkdir -p responses

# Loop through each URL in the file
counter=1
while IFS= read -r url
do
    # Skip empty lines
    [ -z "$url" ] && continue

    # Download the content using wget and store it in a file
    echo "Fetching URL $counter: $url"
    wget -q -O "responses/response_$counter.js" "$url"

    counter=$((counter + 1))
done < "$url_file"

echo "All JS URLs have been processed."
