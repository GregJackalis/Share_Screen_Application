#!/bin/bash

# Set the virtual environment directory
VENV_DIR=Share_Screen_Venv

# Check the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"

    # Change to the directory where your Python script is located
    cd "/Users/grigoriostsakalis/Desktop/College 2023-2024/Networks & Security (Python)/For Assignment/Assignment 1/Share Screen Application (GitHub)"

    # Inform the user that the virtual environment is activated
    echo "Virtual environment activated. You are now in the virtual environment."

    # Keep the script running to keep the virtual environment active
    bash
else
    echo "Unsupported operating system"
    exit 1
fi
