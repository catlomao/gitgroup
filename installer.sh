#!/bin/bash

# URL of the file to download
FILE_URL="https://github.com/catlomao/gitgroup/releases/download/v1/gitgroup"

# Destination path
DESTINATION="/usr/bin/gitgroup"

# Download the file
echo "Downloading file..."
curl -sS -o "/tmp/gitgroup" "$FILE_URL"

# Move the file to /usr/bin (requires sudo)
echo "Moving file to /usr/bin..."
sudo mv "/tmp/gitgroup" "$DESTINATION"

# Ensure it's executable
echo "Setting execute permissions..."
sudo chmod +x "$DESTINATION"

echo "Done!"
