#!/usr/bin/env python3
"""
Resume JSON Publication Updater
------------------------------------
This script updates a Jekyll academic website's resume.json file
with your publications.

Usage:
    python scholar_to_json.py --json_path "path/to/resume.json"

Requirements:
    pip install scholarly==1.7.11 httpx==0.23.0 requests beautifulsoup4 certifi
"""

import argparse
import json
import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def get_publication_list():
    """Return your publications list"""
    logger.info("Using local publications list")
    
    # Your publications list
    return [
        {
            'bib': {
                'title': 'A stochastic simulation of skeletal muscle calcium transients in a structurally realistic sarcomere model using MCell',
                'author': 'Robert John Holash and Brian R MacIntosh',
                'pub_year': '2019',
                'venue': 'PLOS Computational Biology',
                'journal': 'PLOS Computational Biology'
            },
            'pub_url': 'https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006712',
            'num_citations': 5
        },
        {
            'bib': {
                'title': 'In support of the continued use of the term anaerobic threshold',
                'author': 'Brian R MacIntosh and Keenan B MacDougall and Tara M Falconer and R John Holash',
                'pub_year': '2021',
                'venue': 'The Journal of Physiology',
                'journal': 'The Journal of Physiology'
            },
            'pub_url': 'https://physoc.onlinelibrary.wiley.com/doi/epdf/10.1113/JP281262',
            'num_citations': 3
        },
        {
            'bib': {
                'title': 'Technological Breakthroughs in Sport',
                'author': 'Victor R A Cossich and Dave Carlgren and Robert John Holash and Larry Katz',
                'pub_year': '2024',
                'venue': 'Encyclopedia.pub',
                'journal': 'Encyclopedia.pub'
            },
            'pub_url': 'https://encyclopedia.pub/entry/55692',
            'num_citations': 1
        },
        {
            'bib': {
                'title': 'A Ramp- Versus Step-Transition to Constant-Work Rate Exercise Decreases Steady-State Oxygen Uptake',
                'author': 'Gabriele Marinari and Danilo Iannetta and R John Holash and Robin Trama and Robin Faricier and Alessandro M Zagatto and Daniel A Keir and Juan M Murias',
                'pub_year': '2023',
                'venue': 'Medicine and Science in Sport and Exercise',
                'journal': 'Medicine and Science in Sport and Exercise'
            },
            'pub_url': 'https://europepmc.org/article/med/38181214',
            'num_citations': 1
        },
        {
            'bib': {
                'title': 'Heavy-intensity priming exercise extends the V̇o2max plateau and increases peak-power output during ramp-incremental exercise',
                'author': 'Gabriele Marinari and Danilo Iannetta and Robert John Holash and Alessandro M Zagatto and Daniel A Keir and Juan M Murias',
                'pub_year': '2024',
                'venue': 'American Journal of Physiology-Regulatory, Integrative and Comparative Physiology',
                'journal': 'American Journal of Physiology-Regulatory, Integrative and Comparative Physiology'
            },
            'pub_url': 'https://journals.physiology.org/doi/abs/10.1152/ajpregu.00065.2024',
            'num_citations': 0
        },
        {
            'bib': {
                'title': 'Skeletal muscle fatigue–regulation of excitation–contraction coupling to avoid metabolic catastrophe',
                'author': 'BR MacIntosh and RJ Holash',
                'pub_year': '2000',
                'venue': 'Journal of Applied Physiology',
                'journal': 'Journal of Applied Physiology'
            },
            'pub_url': 'https://journals.physiology.org/doi/abs/10.1152/jappl.2000.89.3.1099',
            'num_citations': 142
        },
        {
            'bib': {
                'title': 'A comparison of exergaming interfaces for use in rehabilitation programs and research',
                'author': 'D Levac and D Espy and E Fox and S Pradhan and RJ Holash',
                'pub_year': '2015',
                'venue': 'Journal of Physical Therapy Science',
                'journal': 'Journal of Physical Therapy Science'
            },
            'pub_url': 'https://www.jstage.jst.go.jp/article/jpts/27/3/27_jpts-2014-760/_article/-char/ja/',
            'num_citations': 49
        },
        {
            'bib': {
                'title': 'Power output and force-velocity properties of muscle',
                'author': 'BR MacIntosh and RJ Holash',
                'pub_year': '2009',
                'venue': 'Biomechanics and Biology of Movement',
                'journal': 'Biomechanics and Biology of Movement'
            },
            'pub_url': 'https://books.google.ca/books?hl=en&lr=&id=op91LhcKX-UC&oi=fnd&pg=PA193',
            'num_citations': 35
        },
        {
            'bib': {
                'title': 'Procedures for rat in situ skeletal muscle contractile properties',
                'author': 'BR MacIntosh and PF Gardiner and AJ McComas and RJ Holash',
                'pub_year': '2007',
                'venue': 'Journal of Visualized Experiments',
                'journal': 'Journal of Visualized Experiments'
            },
            'pub_url': 'https://www.jove.com/t/291/procedures-for-rat-in-situ-skeletal-muscle-contractile-properties',
            'num_citations': 29
        },
        {
            'bib': {
                'title': 'Commentaries on Viewpoint: The two-hour marathon: Who and when',
                'author': 'G Millet and H McCubbin and F Danna and M-J Benoit ... and RJ Holash and others',
                'pub_year': '2011',
                'venue': 'Journal of Applied Physiology',
                'journal': 'Journal of Applied Physiology'
            },
            'pub_url': 'https://journals.physiology.org/doi/full/10.1152/japplphysiol.00563.2011',
            'num_citations': 21
        },
        {
            'bib': {
                'title': 'Three dimensional stochastic computer model of the skeletal muscle half sarcomere: Changes in calcium diffusion caused by the myofilament lattice',
                'author': 'RJ Holash and BR MacIntosh',
                'pub_year': '2018',
                'venue': 'FASEB Journal',
                'journal': 'FASEB Journal'
            },
            'pub_url': '',
            'num_citations': 1
        },
        {
            'bib': {
                'title': 'An innovative ergometer to measure neuromuscular fatigue immediately after cycling',
                'author': 'JC Chien and RJ Holash and T Emese Ökrös and S-Z Tsong and Y-C Chang and Y-R Lin',
                'pub_year': '2016',
                'venue': 'Journal of Visualized Experiments',
                'journal': 'Journal of Visualized Experiments'
            },
            'pub_url': 'https://www.jove.com/t/54037/an-innovative-ergometer-to-measure-neuromuscular-fatigue-immediately',
            'num_citations': 4
        }
    ]

def format_for_resume_json(publications):
    """
    Format publications into resume.json format
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
        # Check if file exists
        if not os.path.exists(json_path):
            logger.warning(f"File not found: {json_path}")
            # Try to find the correct path in common locations
            possible_paths = [
                os.path.join(os.path.dirname(json_path), "resume.json"),
                os.path.join(os.path.dirname(os.path.dirname(json_path)), "assets", "json", "resume.json"),
                os.path.join(os.path.dirname(os.path.dirname(json_path)), "assets", "json", "johnresume.json")
            ]
            
            for path in possible_paths:
                if os.path.exists(path):
                    logger.info(f"Found resume.json at: {path}")
                    json_path = path
                    break
            else:
                # Create a new file if none exists
                logger.warning("Could not find resume.json, will create a new one")
                resume_data = {"publications": []}
                
                # Write updated data to file
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(resume_data, f, indent=2, ensure_ascii=False)
                    
                logger.info(f"Created new resume.json at {json_path}")
        
        # Read existing resume.json if it exists
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                resume_data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # If file doesn't exist or is invalid JSON, create a new one
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
        # Convert release dates to comparable strings to avoid type comparison issues
        def get_sort_key(pub):
            date = pub.get('releaseDate', '')
            if not date:
                return '0'
            try:
                # Convert to string first to avoid int/str comparison errors
                return str(date).zfill(4)
            except:
                return '0'  # Default if conversion fails
                
        resume_data['publications'] = sorted(
            resume_data['publications'], 
            key=get_sort_key, 
            reverse=True
        )
        
        # Write updated data back to file
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(resume_data, f, indent=2, ensure_ascii=False)
            
        logger.info(f"Updated resume.json at {json_path} with {new_count} new publications")
        return True
    except Exception as e:
        logger.error(f"Error updating resume.json: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Update resume.json with publications')
    parser.add_argument('--json_path', required=True, help='Path to resume.json file')
    args = parser.parse_args()
    
    # Get publications list
    publications = get_publication_list()
    
    # Format publications for resume.json
    formatted_pubs = format_for_resume_json(publications)
    
    # Update resume.json
    update_resume_json(args.json_path, formatted_pubs)
    
    logger.info("Script completed")

if __name__ == "__main__":
    main()
