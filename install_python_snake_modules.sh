#!/bin/bash

# Check if sudo is available
if ! command -v sudo &> /dev/null; then
    echo "sudo is not available. Please make sure you have administrative privileges."
    exit 1
fi

# Update package list and install Python 3
sudo apt update
sudo apt install -y python3 python3-pip

# Install Playsound modules
pip3 install playsound

echo "Installation completed."

