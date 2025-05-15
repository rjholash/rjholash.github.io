# Deployment Guide

This guide explains how to deploy and publish updates to your website.

## Table of Contents

1. [GitHub Pages Deployment](#github-pages-deployment)
2. [Local Testing](#local-testing)
3. [Deployment Process](#deployment-process)
4. [Common Deployment Issues](#common-deployment-issues)

## GitHub Pages Deployment

Your website (rjholash.github.io) is hosted on GitHub Pages, which automatically builds and deploys your site when changes are pushed to the main branch.

### How It Works

1. You push changes to your GitHub repository
2. GitHub runs Jekyll to build your website
3. The built site is published to the URL: https://rjholash.github.io

### Repository Settings

Your repository should have GitHub Pages enabled with these settings:

1. **Source**: Deploy from a branch
2. **Branch**: main
3. **Folder**: / (root)

You can verify these settings by going to:
Repository → Settings → Pages

## Local Testing

Before pushing changes, it's a good idea to test your website locally.

### Initial Setup for Local Testing

1. Install Ruby and Jekyll (if not already installed):
   - [Ruby Installation Guide](https://jekyllrb.com/docs/installation/)
   - [Jekyll Installation Guide](https://jekyllrb.com/docs/)

2. Install dependencies:
   ```bash
   cd /path/to/rjholash.github.io
   bundle install
   ```

### Running the Site Locally

1. Navigate to your website directory:
   ```bash
   cd /path/to/rjholash.github.io
   ```

2. Start the Jekyll server:
   ```bash
   bundle exec jekyll serve
   ```

3. View your website at: http://localhost:4000

4. Press Ctrl+C to stop the server when finished

## Deployment Process

Follow these steps to deploy changes to your live website:

### Using Git on the Command Line

1. Make and test your changes locally
2. Stage the changed files:
   ```bash
   git add .
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of your changes"
   ```
4. Push to GitHub:
   ```bash
   git push origin main
   ```
5. Wait a few minutes for GitHub Pages to build and deploy your site
6. Visit https://rjholash.github.io to verify your changes

### Using GitHub Desktop

1. Make and test your changes locally
2. Open GitHub Desktop
3. Review changed files
4. Enter a commit message describing your changes
5. Click "Commit to main"
6. Click "Push origin"
7. Wait a few minutes for deployment to complete
8. Visit your site to verify changes

### Checking Deployment Status

1. Go to your GitHub repository
2. Click on the "Actions" tab
3. Look for the latest workflow run to see if deployment was successful

## Common Deployment Issues

### Build Failures

If your site fails to build, check:

1. **GitHub Actions tab** for error messages
2. **Invalid YAML formatting** in data files or front matter
3. **Missing dependencies** in your Gemfile
4. **Ruby version incompatibilities**

### Content Not Updating

If your site builds but content isn't updating:

1. **Verify your changes** were committed and pushed
2. **Clear your browser cache** or use incognito mode
3. **Check file paths** for case sensitivity issues
4. **Ensure front matter** is correctly formatted

### Missing Images or Assets

If images or assets aren't appearing:

1. **Check file paths** in your Markdown
2. **Verify assets** were committed to the repository
3. **Check for case sensitivity** in file paths

### Jekyll Build Errors

Common Jekyll build errors include:

1. **Liquid syntax errors** in templates
2. **Front matter formatting issues**
3. **Invalid UTF-8 characters** in files
4. **Plugin compatibility problems**

If you encounter specific errors, consult the [Jekyll troubleshooting guide](https://jekyllrb.com/docs/troubleshooting/).
