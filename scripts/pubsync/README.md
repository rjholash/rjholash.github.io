# Cross-Platform Publication Sync Tool

This tool synchronizes publications from the BibTeX file (`_bibliography/papers.bib`) to the CV YAML file (`_data/cv.yml`), allowing you to maintain a single source of truth for all your publications. It works on **Windows, macOS, and Linux**.

## Quick Start

### First-Time Setup

Run the setup script to install dependencies and configure the environment:

- **Windows**: Double-click `setup.py` or run `python setup.py` in a terminal
- **macOS/Linux**: Run `python3 setup.py` in a terminal

### Running the Sync Tool

After adding new publications to your BibTeX file, run the sync tool:

- **Windows**: Double-click `sync_publications.bat`
- **macOS/Linux**: Run `./sync_publications.sh` in a terminal

## How It Works

1. The script reads your BibTeX file and extracts publication information
2. It formats the data appropriately for your CV file
3. It updates the CV YAML file with the publications data
4. Publications are sorted by year (newest first)

## Detailed Usage Instructions

### Prerequisites

- Python 3.6 or higher
- Required packages: `bibtexparser`, `pyyaml` (installed automatically by the setup script)

### Running on Windows

1. Open Windows Explorer to `scripts/pubsync`
2. Double-click on `sync_publications.bat`
3. Wait for the process to complete
4. Check your `_data/cv.yml` file to verify the changes

### Running on macOS

1. Open Terminal
2. Navigate to the scripts directory:
   ```bash
   cd path/to/your/website/scripts/pubsync
   ```
3. Make the script executable (first time only):
   ```bash
   chmod +x sync_publications.sh
   ```
4. Run the script:
   ```bash
   ./sync_publications.sh
   ```

### Running on Linux

1. Open Terminal
2. Navigate to the scripts directory:
   ```bash
   cd path/to/your/website/scripts/pubsync
   ```
3. Make the script executable (first time only):
   ```bash
   chmod +x sync_publications.sh
   ```
4. Run the script:
   ```bash
   ./sync_publications.sh
   ```

### Running the Python Script Directly (All Platforms)

If you prefer to run the Python script directly:

1. Open a terminal/command prompt
2. Navigate to the scripts directory:
   ```
   cd path/to/your/website/scripts/pubsync
   ```
3. Run the script:
   - Windows: `python bibtex_to_cv.py`
   - macOS/Linux: `python3 bibtex_to_cv.py`

## Workflow for Adding New Publications

1. Add the new publication to `_bibliography/papers.bib` using BibTeX format
2. Run the sync script using the method for your platform
3. Check your CV page to verify the publication appears correctly
4. Commit both files to your git repository

## Excluding Publications from CV

If you want a publication to appear only on the Publications page but not in your CV:

1. Add `keywords = {nocv}` to the BibTeX entry
2. Run the sync script again

Example:
```bibtex
@inproceedings{conference2023,
    title = {Example Conference Presentation},
    author = {Holash, Robert John},
    booktitle = {Conference Proceedings},
    year = {2023},
    keywords = {nocv}
}
```

## Troubleshooting

### Common Issues

- **Script Not Finding Files**: The script tries to automatically locate your website root directory. If it can't find it, it will prompt you to enter the path manually.

- **Missing Dependencies**: If you see errors about missing packages, run:
  - Windows: `pip install bibtexparser pyyaml`
  - macOS/Linux: `pip3 install bibtexparser pyyaml`

- **Permission Errors on macOS/Linux**: Make the scripts executable:
  ```bash
  chmod +x bibtex_to_cv.py sync_publications.sh
  ```

- **Formatting Issues**: The script tries to clean LaTeX formatting; check if any special formatting needs custom handling.

### Platform-Specific Issues

#### Windows Issues

- **Python Not Found**: Ensure Python is installed and added to your PATH
- **Script Won't Run**: Try running from Command Prompt or PowerShell instead of double-clicking

#### macOS Issues

- **"Operation not permitted"**: Run the script with proper permissions
- **Python Version**: macOS might have Python 2 as default; use `python3` explicitly

#### Linux Issues

- **Script Not Executable**: Run `chmod +x script_name` to make scripts executable
- **Missing Python**: Install Python 3 via your distribution's package manager

## Customization

If you need to customize how publications appear in your CV, edit the Python script:

1. Open `bibtex_to_cv.py` in a text editor
2. Look for the `convert_bibtex_to_cv_format` function
3. Modify it to change formatting, fields, or sorting logic

