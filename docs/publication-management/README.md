# Publication Management System

This guide explains how to manage publications on the website, including the cross-platform publication sync system that keeps your CV and publications list in sync.

## Table of Contents

1. [System Overview](#system-overview)
2. [How Publications Work](#how-publications-work)
3. [Using the Publication Sync System](#using-the-publication-sync-system)
4. [Cross-Platform Instructions](#cross-platform-instructions)
5. [Advanced Options](#advanced-options)
6. [Troubleshooting](#troubleshooting)

## System Overview

The website uses a two-part system for publications:

1. **BibTeX File** (`_bibliography/papers.bib`): The primary source of truth for all publications
2. **CV YAML File** (`_data/cv.yml`): Contains CV information including publications

The Publication Sync System automatically synchronizes publications from the BibTeX file to the CV YAML file, allowing you to maintain only one file while keeping both the Publications page and CV page up-to-date.

## How Publications Work

### Publications Page

- Uses the Jekyll-Scholar plugin
- Sources data from `_bibliography/papers.bib`
- Configured in `_config.yml` under the `scholar` section
- Publications are displayed using the `bib.liquid` layout

### CV Page

- Uses the `cv.yml` file from `_data` directory
- The "papers" section contains publication data
- Publications are displayed using the `cv.liquid` layout

## Using the Publication Sync System

### First-Time Setup

Run the setup script once to install dependencies and configure the environment:

1. Navigate to the `scripts/pubsync` directory
2. Run the setup script:
   - **Windows**: Double-click `setup.py` or run `python setup.py` in a terminal
   - **macOS/Linux**: Run `python3 setup.py` in a terminal

### Regular Usage

After adding new publications to your BibTeX file, run the appropriate script for your platform:

- **Windows**: Double-click `sync_publications.bat`
- **macOS/Linux**: Run `./sync_publications.sh` (make sure it's executable with `chmod +x sync_publications.sh`)

### Publication Workflow

1. Add the new publication to `_bibliography/papers.bib` using BibTeX format
2. Run the sync script using the method for your current platform
3. Check your website to verify the publication appears correctly on both pages
4. Commit both files to your git repository

## Cross-Platform Instructions

### Windows Instructions

1. Open Windows Explorer to `scripts/pubsync`
2. Double-click on `sync_publications.bat`
3. Wait for the process to complete
4. Check your `_data/cv.yml` file to verify the changes

### macOS Instructions

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

### Linux Instructions

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

### Using the Python Script Directly (All Platforms)

If you prefer to run the Python script directly:

1. Open a terminal/command prompt
2. Navigate to the scripts directory:
   ```
   cd path/to/your/website/scripts/pubsync
   ```
3. Run the script:
   - Windows: `python bibtex_to_cv.py`
   - macOS/Linux: `python3 bibtex_to_cv.py`

## Advanced Options

### Excluding Publications from CV

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

### Customizing the Script

If you need to change how publications appear in your CV:

1. Edit the `convert_bibtex_to_cv_format` function in `bibtex_to_cv.py`
2. You can modify field formatting, add/remove fields, or change sorting logic

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
