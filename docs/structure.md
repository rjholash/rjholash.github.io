# Website Structure

This document provides an overview of the website's structure and key components.

## Directory Structure

The website is built using Jekyll with the al-folio theme. Here's an overview of the key directories and files:

```
rjholash.github.io/
├── _bibliography/     # BibTeX publications data
├── _data/             # Site data files (CV, venues, etc.)
├── _includes/         # Template components
├── _layouts/          # Page layouts
├── _pages/            # Content pages
├── _posts/            # Blog posts
├── _projects/         # Project descriptions
├── _sass/             # CSS styling
├── assets/            # Static assets (images, PDFs, etc.)
├── docs/              # Website maintenance documentation
├── scripts/           # Utility scripts for maintenance
├── _config.yml        # Main site configuration
└── README.md          # Project README
```

## Key Files and Directories

### Content Management

- **`_bibliography/papers.bib`**: The BibTeX file containing all publications.
- **`_data/cv.yml`**: Your CV information in YAML format.
- **`_pages/`**: Contains the main content pages of the website.
- **`_posts/`**: Blog posts (if used).
- **`_projects/`**: Project descriptions.

### Configuration and Layout

- **`_config.yml`**: Main configuration file for the Jekyll site.
- **`_layouts/`**: Page layout templates.
- **`_includes/`**: Reusable components included in layouts.

### Assets and Styling

- **`assets/`**: Contains images, PDFs, and other static files.
- **`_sass/`**: CSS styling for the website.

### Maintenance

- **`docs/`**: Documentation for maintaining the website.
- **`scripts/`**: Utility scripts for website maintenance.

## Important Pages

The main pages of the website are defined in the `_pages/` directory:

- **`about.md`**: The home page with your profile.
- **`cv.md`**: Your CV page.
- **`publications.md`**: List of publications.
- **`projects.md`**: Portfolio of projects.
- **`teaching.md`**: Teaching information.

## Data Files

The `_data/` directory contains structured data used throughout the site:

- **`cv.yml`**: Your CV information.
- **`venues.yml`**: Publication venue information.
- **`coauthors.yml`**: Information about your coauthors.

## How Jekyll Builds the Site

1. Jekyll reads the configuration from `_config.yml`
2. It processes Markdown files in `_pages/` and other collections
3. It applies the layouts from `_layouts/`
4. It includes components from `_includes/`
5. The Jekyll-Scholar plugin processes `papers.bib` for the publications page
6. The final HTML site is generated in the `_site/` directory (not committed to git)

## Customizing the Website

If you want to customize the website's appearance or behavior:

1. **Content changes**: Edit files in `_pages/`, `_posts/`, or `_projects/`
2. **Layout changes**: Modify templates in `_layouts/` or components in `_includes/`
3. **Styling changes**: Edit the SCSS files in `_sass/`
4. **Config changes**: Update settings in `_config.yml`

## Deployment

The website is deployed using GitHub Pages. When you push changes to the main branch, GitHub automatically builds and deploys the site.
