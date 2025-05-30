# Google Scholar to Resume.json Automation

This tool automatically updates your website's publication list by scraping your Google Scholar profile and updating your `resume.json` file. It runs weekly via GitHub Actions to keep your website's publication list current with minimal effort.

## Features

- Automatically retrieves all publications from your Google Scholar profile
- Formats publication data to match the resume.json schema used by your Jekyll website
- Preserves existing resume data while adding new publications
- Can be run manually or automatically via GitHub Actions
- Handles proper formatting of authors, titles, venues, and more
- Adds publication links, DOIs, and citation counts when available

## Manual Usage

If you want to run the update manually, you can:

1. Install the required Python packages:

   ```bash
   pip install scholarly==1.7.11 httpx==0.23.0 requests beautifulsoup4
   ```

2. Run the script:
   ```bash
   python scripts/scholar_to_json.py --json_path "assets/json/resume.json"
   ```

Your Google Scholar ID (`Qx4U24oAAAAJ`) is already configured in the script.

## Automated Updates

The included GitHub Actions workflow (`update-scholar.yml`) will run automatically every Sunday at 1:00 AM UTC to check for new publications and update your resume.json file.

You can also trigger a manual update by:

1. Going to your GitHub repository
2. Clicking on the "Actions" tab
3. Selecting the "Update Resume from Google Scholar" workflow
4. Clicking "Run workflow"

## Troubleshooting

- **Google Scholar Blocking**: If you encounter blocks from Google Scholar, the script uses free proxies to avoid detection. You might need to adjust the delay settings if you're still experiencing issues.
- **Missing Publications**: Some publications might not appear if they're missing key information. Check the script logs for details.
- **JSON Format Issues**: If the script has problems with your resume.json structure, you may need to modify the code.

## Technical Details

The `scholar_to_json.py` script:

1. Uses the `scholarly` Python library to access Google Scholar
2. Retrieves your profile and all associated publications
3. Formats each publication to match the resume.json schema
4. Adds new publications to your existing resume.json file
5. Sorts publications by date (newest first)
