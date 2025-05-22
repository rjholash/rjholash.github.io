#!/usr/bin/env python3
"""
Script to sync publications from papers.bib to cv.yml
This allows maintaining a single source of truth for publications.
Platform-independent - works on Windows, Mac, and Linux.
"""

import bibtexparser
import yaml
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Determine the project root path regardless of platform
def find_project_root():
    """Find the project root directory containing _bibliography and _data folders."""
    # Start with the directory containing this script
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    
    # Navigate up until we find the project root (containing _bibliography and _data)
    while current_dir != current_dir.parent:
        if (current_dir / '_bibliography').exists() and (current_dir / '_data').exists():
            return current_dir
        current_dir = current_dir.parent
    
    # If we couldn't find it automatically, try the relative path from the script
    script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    potential_root = script_dir.parent.parent
    if (potential_root / '_bibliography').exists() and (potential_root / '_data').exists():
        return potential_root
        
    # If still not found, ask the user
    print("Error: Could not automatically find project root directory.")
    print("Please enter the full path to your website root directory:")
    user_path = input("> ").strip()
    user_path = Path(user_path)
    if (user_path / '_bibliography').exists() and (user_path / '_data').exists():
        return user_path
    else:
        print("Error: The provided path doesn't appear to be a valid website root.")
        print("The directory should contain _bibliography and _data folders.")
        sys.exit(1)

# Get the project root path
PROJECT_ROOT = find_project_root()

# File paths using Path objects for cross-platform compatibility
BIBTEX_PATH = PROJECT_ROOT / '_bibliography' / 'papers.bib'
CV_PATH = PROJECT_ROOT / '_data' / 'cv.yml'

def load_bibtex():
    """Load BibTeX file and parse entries."""
    with open(BIBTEX_PATH, 'r', encoding='utf-8') as bibtex_file:
        # Skip YAML front matter if present
        content = bibtex_file.read()
        # Remove YAML front matter if present
        content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
        
        # Parse BibTeX content
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = False
        parser.homogenize_fields = False
        bib_database = bibtexparser.loads(content, parser)
        return bib_database.entries

def load_cv():
    """Load the current CV YAML file."""
    try:
        with open(CV_PATH, 'r', encoding='utf-8') as yml_file:
            cv_data = yaml.safe_load(yml_file)
            return cv_data
    except Exception as e:
        print(f"Error loading CV file: {e}")
        print(f"Creating new CV file at {CV_PATH}")
        # Return empty dict if file doesn't exist or has issues
        return {}

def save_cv(cv_data):
    """Save the updated CV YAML file."""
    # Ensure the _data directory exists
    os.makedirs(os.path.dirname(CV_PATH), exist_ok=True)
    
    with open(CV_PATH, 'w', encoding='utf-8') as yml_file:
        yaml.dump(cv_data, yml_file, default_flow_style=False, sort_keys=False, allow_unicode=True)

def clean_latex(text):
    """Clean LaTeX formatting from text."""
    if not text:
        return ""
    # Remove braces
    text = re.sub(r'{|}', '', text)
    # Remove LaTeX commands
    text = re.sub(r'\\[a-zA-Z]+', '', text)
    # Fix spacing
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def format_authors(authors_str):
    """Format BibTeX author string to readable format."""
    if not authors_str:
        return ""
    # Split by 'and' and clean each author name
    authors = [name.strip() for name in authors_str.split(' and ')]
    # Format each author as "Firstname Lastname"
    formatted_authors = []
    for author in authors:
        parts = author.split(',')
        if len(parts) > 1:
            # Format "Lastname, Firstname" to "Firstname Lastname"
            formatted_authors.append(f"{parts[1].strip()} {parts[0].strip()}")
        else:
            # If no comma, assume already in correct format
            formatted_authors.append(author)
    # Join with commas
    return ', '.join(formatted_authors)

def get_journal(entry):
    """Extract journal or publication venue from entry."""
    if 'journal' in entry:
        return clean_latex(entry['journal'])
    elif 'booktitle' in entry:
        return clean_latex(entry['booktitle'])
    elif 'publisher' in entry:
        return clean_latex(entry['publisher'])
    return ""

def convert_bibtex_to_cv_format(bibtex_entries):
    """Convert BibTeX entries to CV YAML format."""
    cv_papers = []
    
    # Sort entries by year (newest first)
    bibtex_entries.sort(key=lambda x: int(x.get('year', '0')), reverse=True)
    
    for entry in bibtex_entries:
        # Skip entries without title or year
        if not entry.get('title') or not entry.get('year'):
            continue
        
        # Check if entry should be included in CV (default to True)
        include_in_cv = True
        if 'keywords' in entry:
            keywords = entry.get('keywords', '').lower()
            # Exclude entries tagged with 'nocv'
            if 'nocv' in keywords:
                include_in_cv = False
        
        if not include_in_cv:
            continue
        
        # Format authors
        authors = format_authors(entry.get('author', ''))
        
        # Create CV paper entry
        paper = {
            'title': clean_latex(entry.get('title', '')),
            'authors': authors,
            'journal': get_journal(entry),
            'year': entry.get('year', '')
        }
        
        # Add optional fields if they exist
        if 'doi' in entry:
            paper['doi'] = entry.get('doi').strip()
            
        if 'volume' in entry:
            paper['volume'] = entry.get('volume')
            
        if 'number' in entry:
            paper['issue'] = entry.get('number')
            
        # Add all pages if both start and end are specified
        if 'pages' in entry:
            pages = entry.get('pages', '')
            # Format pages properly
            if '--' in pages or '-' in pages:
                pages = pages.replace('--', '-')
                paper['pages'] = pages
            else:
                paper['pages'] = pages
                
        # Add URL if available
        if 'url' in entry:
            paper['url'] = entry.get('url')
        elif 'doi' in entry:
            paper['url'] = f"https://doi.org/{entry.get('doi')}"
        elif 'html' in entry:
            paper['url'] = entry.get('html')
            
        cv_papers.append(paper)
    
    return cv_papers

def update_cv_with_publications(cv_data, cv_papers):
    """Update the CV data with the new publications list."""
    # Check if papers key exists in CV
    if 'papers' in cv_data:
        cv_data['papers'] = cv_papers
    else:
        # Add papers section at the end
        cv_data['papers'] = cv_papers
    
    return cv_data

def main():
    """Main function to synchronize BibTeX to CV YAML."""
    print(f"Synchronizing publications from {BIBTEX_PATH} to {CV_PATH}...")
    
    try:
        # Load data
        bibtex_entries = load_bibtex()
        cv_data = load_cv()
        
        # Convert BibTeX to CV format
        cv_papers = convert_bibtex_to_cv_format(bibtex_entries)
        
        # Update CV with publications
        cv_data = update_cv_with_publications(cv_data, cv_papers)
        
        # Save updated CV
        save_cv(cv_data)
        
        print(f"Successfully updated {len(cv_papers)} publications in {CV_PATH}")
        print(f"Note: To exclude a publication from CV, add 'keywords = {{nocv}}' to its BibTeX entry.")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    
    # Keep terminal window open on Windows if run by double-clicking
    if os.name == 'nt' and 'pythonw' not in sys.executable.lower():
        if not sys.stdin.isatty():
            print("\nPress Enter to exit...")
            input()
