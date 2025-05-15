#!/bin/bash
# Cross-platform publication sync script for Mac/Linux
# File: sync_publications.sh

# Determine script directory regardless of where it's called from
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "====================================================="
echo "Publication Sync: BibTeX to CV.yml"
echo "====================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not found."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Install required Python packages if not already installed
pip3 install bibtexparser pyyaml 2>/dev/null || pip install bibtexparser pyyaml

# Run the sync script
python3 "$SCRIPT_DIR/bibtex_to_cv.py" || python "$SCRIPT_DIR/bibtex_to_cv.py"

echo
echo "Sync process completed!"
echo

# Make the script executable
chmod +x "$SCRIPT_DIR/bibtex_to_cv.py"
