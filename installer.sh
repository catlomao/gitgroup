#!/bin/bash

# Destination path
DESTINATION="/usr/bin/gitgroup"

# Download the file
echo "Downloading file..."
curl -L -o /tmp/gitgroup "https://github.com/catlomao/gitgroup/releases/download/v1/gitgroup"

# Move the file to /usr/bin (requires sudo)
echo "Moving file to /usr/bin..."
sudo mv "/tmp/gitgroup" "$DESTINATION"

# Ensure it's executable
echo "Setting execute permissions..."
sudo chmod +x "$DESTINATION"

echo "Done!"
