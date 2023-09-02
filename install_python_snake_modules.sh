#!/bin/bash

# Check for administrative privileges
if [ "$EUID" -ne 0 ]; then
    echo "This script requires administrative privileges. Please run it as root or with sudo."
    exit 1
fi

# Update package list and install Python 3 and Pygame
apt update
apt install -y python3 python3-pip
pip3 install pygame

echo "Installation completed."