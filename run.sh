#!/bin/bash

echo "Starting Selenium Tests..."

# Detect operating system and set appropriate script path
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    # Unix-based paths (e.g., GitHub Actions, Linux, macOS)
    script_path="/home/runner/work/LoginTest/LoginTest"
elif [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "win32"* ]]; then
    # Windows-based paths (e.g., Git Bash or WSL)
    script_path="C:/Users/jebas/LoginTest"
else
    echo "Unsupported OS type: $OSTYPE"
    exit 1
fi

# Print the script path for debugging
echo "Using script path: $script_path"

# Add LoginTest to PYTHONPATH for module import
export PYTHONPATH="$script_path"

# Ensure the script runs in the project root directory
cd "$(dirname "$0")"

# Exit if any command fails
set -e

echo "Installing dependencies..."
# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
    echo "ERROR: requirements.txt not found in $(pwd). Please ensure it exists."
    exit 1
fi

# Install dependencies
pip install --user -r requirements.txt

echo "Running Selenium tests..."
# Check if the test file exists
if [ ! -f tests/test_example.py ]; then
    echo "ERROR: Test file 'tests/test_example.py' not found."
    exit 1
fi

# Run Selenium tests
python tests/test_example.py

echo "Selenium tests completed successfully!"

