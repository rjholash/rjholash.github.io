#!/usr/bin/env python3
"""
Google Scholar to Resume JSON Updater
------------------------------------
This script automatically updates a Jekyll academic website's resume.json file
with publications from Google Scholar.

Usage:
    python scholar_to_json.py --json_path "path/to/resume.json"

Requirements:
    pip install scholarly requests beautifulsoup4
"""

import argparse
import json
import os
from datetime import datetime
import time
import random
import logging
from scholarly import scholarly, ProxyGenerator

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def setup_proxy():
    """Set up a proxy to avoid Google Scholar blocks"""
    try:
        pg = ProxyGenerator()
        
        # Try to use Tor if available
        success = pg.Tor_Internal(tor_cmd="tor")
        if success:
            logger.info("Using Tor as proxy")
            scholarly.use_proxy(pg)
            return True
            
        # Otherwise try free proxies
        # Use a more conservative approach that should work with any version
        scholarly.use_proxy(None)  # Reset proxy settings
        logger.info("Not using any proxy - direct connection")
        return True
    except Exception as e:
        logger.error(f"Error setting up proxy: {e}")
        # Continue without proxy
        scholarly.use_proxy(None)
        return True

def get_scholar_publications(scholar_id):
    """
    Retrieve publications from a Google Scholar profile
    """
    logger.info(f"Retrieving publications for Scholar ID: {scholar_id}")
    
    try:
        # Search for the author by ID
        author = scholarly.search_author_id(scholar_id)
        if not author:
            logger.error(f"No author found with ID {scholar_id}")
            return []
            
        # Fill in all available author data
        author = scholarly.fill(author)
        
        # Extract publications
        publications = author.get('publications', [])
        
        # Get complete information for each publication
        complete_publications = []
        total_pubs = len(publications)
        
        logger.info(f"Found {total_pubs} publications. Retrieving details...")
        
        for i, pub in enumerate(publications):
            logger.info(f"Processing publication {i+1}/{total_pubs}: {pub.get('bib', {}).get('title', 'Unknown title')}")
            try:
                # Fill in publication details
                filled_pub = scholarly.fill(pub)
                complete_publications.append(filled_pub)
                
                # Add a random delay to avoid triggering Google Scholar's anti-scraping measures
                time.sleep(random.uniform(1, 3))
            except Exception as e:
                logger.error(f"Error retrieving details for publication: {e}")
        
        return complete_publications
    except Exception as e:
        logger.error(f"Error retrieving publications: {e}")
        return []

def format_for_resume_json(publications):
    """
    Format Google Scholar publications into resume.json format
    """
    formatted_publications = []
    
    for pub in publications:
        bib = pub.get('bib', {})
        
        # Skip if missing essential info
        if not bib.get('title') or not bib.get('author'):
            continue
            
        # Format authors
        authors = bib.get('author', '').split(' and ')
        
        # Create entry
        entry = {
            "name": bib.get('title', ''),
            "publisher": bib.get('journal', bib.get('venue', 'Unknown venue')),
            "releaseDate": bib.get('pub_year', ''),
            "website": pub.get('pub_url', ''),
            "summary": bib.get('abstract', ''),
        }
        
        # Add authors
        if authors:
            entry["authors"] = authors
            
        # Add DOI if available
        if pub.get('doi'):
            entry["doi"] = pub.get('doi')
            
        # Add citation count if available
        if pub.get('num_citations'):
            entry["citationCount"] = pub.get('num_citations')
            
        formatted_publications.append(entry)
    
    return formatted_publications

def update_resume_json(json_path, publications):
    """
    Update the resume.json file with new publications
    """
    try:
        # Read existing resume.json
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                resume_data = json.load(f)
        else:
            resume_data = {}
        
        # Update publications section
        if 'publications' not in resume_data:
            resume_data['publications'] = []
            
        # Add each publication if it doesn't already exist (by title)
        existing_titles = {pub.get('name', '') for pub in resume_data['publications']}
        new_count = 0
        
        for pub in publications:
            if pub['name'] not in existing_titles:
                resume_data['publications'].append(pub)
                existing_titles.add(pub['name'])
                new_count += 1
        
        # Sort publications by release date (newest first)
        resume_data['publications'] = sorted(
            resume_data['publications'], 
            key=lambda x: x.get('releaseDate', '0'), 
            reverse=True
        )
        
        # Write updated data back to file
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(resume_data, f, indent=2, ensure_ascii=False)
            
        logger.info(f"Updated resume.json with {new_count} new publications")
        return True
    except Exception as e:
        logger.error(f"Error updating resume.json: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Update resume.json with Google Scholar publications')
    parser.add_argument('--scholar_id', default='sqI9lDoAAAAJ', help='Google Scholar ID')
    parser.add_argument('--json_path', required=True, help='Path to resume.json file')
    args = parser.parse_args()
    
    # Set up proxy to avoid being blocked
    setup_proxy()
    
    # Get publications from Google Scholar
    publications = get_scholar_publications(args.scholar_id)
    
    if not publications:
        logger.warning("No publications found or error occurred")
        return
    
    # Format publications for resume.json
    formatted_pubs = format_for_resume_json(publications)
    
    # Update resume.json
    update_resume_json(args.json_path, formatted_pubs)
    
    logger.info("Script completed")

if __name__ == "__main__":
    main()
