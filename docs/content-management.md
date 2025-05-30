# Content Management Guide

This guide explains how to update and manage different types of content on the website.

## Table of Contents

1. [CV Information](#cv-information)
2. [Projects](#projects)
3. [Blog Posts](#blog-posts)
4. [Images and Assets](#images-and-assets)
5. [Custom Pages](#custom-pages)

## CV Information

The CV information is stored in the YAML file at `_data/cv.yml`. This file contains structured data that appears on your CV page.

### Updating CV Sections

1. Open `_data/cv.yml` in a text editor
2. Edit the relevant sections:
   - `general`: Your name, title, and contact information
   - `education`: Your educational background
   - `experience`: Your work experience
   - `papers`: Your publications (this is automatically updated by the Publication Sync Tool)
   - `conferences`: Your conference presentations

### CV Format

The YAML format uses indentation to indicate structure. Be careful to maintain proper indentation when editing. For example:

```yaml
general:
  name: "Dr. Robert John Holash"
  title: "Assistant Professor (Teaching)"
  department: "Faculty of Kinesiology"
  institution: "University of Calgary"
  email: "rjholash@ucalgary.ca"
  location: "Calgary, Alberta, Canada"

education:
  - degree: "PhD in Muscle Physiology"
    institution: "University of Calgary"
    year: 2017
    thesis: "Three dimensional stochastic computer model..."
```

### Adding New CV Sections

If you want to add a new section to your CV:

1. Add a new top-level entry to the `cv.yml` file
2. Then, modify the CV template at `_layouts/cv.liquid` to display the new section

## Projects

Projects are stored as individual Markdown files in the `_projects/` directory.

### Adding a New Project

1. Create a new Markdown file in the `_projects/` directory
2. Include the required front matter:

```yaml
---
layout: page
title: Project Title
description: Brief description of the project
img: assets/img/project-thumbnail.jpg
importance: 1
category: work
---
```

3. Add the project content in Markdown format below the front matter

### Project Front Matter Options

- `layout`: Always set to "page"
- `title`: Project title
- `description`: Brief description of the project
- `img`: Path to the thumbnail image (relative to the site root)
- `importance`: Used for ordering projects (1 = highest)
- `category`: Project category (e.g., work, fun, research)
- `redirect`: Optional, URL to redirect to for external projects

### Updating Existing Projects

1. Find the project file in the `_projects/` directory
2. Edit the front matter or content as needed
3. Save the file

## Blog Posts

Blog posts are stored as Markdown files in the `_posts/` directory.

### Adding a New Blog Post

1. Create a new Markdown file in the `_posts/` directory
2. Name the file with the format: `YYYY-MM-DD-title.md`
3. Include the required front matter:

```yaml
---
layout: post
title: Post Title
date: YYYY-MM-DD HH:MM:SS-0500
description: Brief description of the post
tags: tag1 tag2
categories: category1
---
```

4. Add the post content in Markdown format below the front matter

### Post Front Matter Options

- `layout`: Always set to "post"
- `title`: Post title
- `date`: Publication date and time
- `description`: Brief description
- `tags`: List of tags for classification
- `categories`: List of categories
- `related_posts`: Set to true to show related posts

## Images and Assets

Images and other files (PDFs, documents, etc.) are stored in the `assets/` directory.

### Adding Images

1. Place image files in the `assets/img/` directory
2. For project thumbnails, consider using the `assets/img/projects/` subdirectory
3. Reference images in Markdown using:
   ```markdown
   ![Description](/assets/img/filename.jpg)
   ```

### Adding PDF Documents

1. Place PDF files in the `assets/pdf/` directory
2. Link to PDFs in Markdown using:
   ```markdown
   [Link Text](/assets/pdf/filename.pdf)
   ```

### Image Optimization

For better performance, optimize images before adding them:

1. Resize images to an appropriate size (e.g., 1200px max width for regular images)
2. Use JPEG for photographs and PNG for graphics with transparency
3. Compress images using tools like TinyPNG or ImageOptim

## Custom Pages

Custom pages are stored as Markdown files in the `_pages/` directory.

### Adding a New Page

1. Create a new Markdown file in the `_pages/` directory
2. Include the required front matter:

```yaml
---
layout: page
permalink: /page-url/
title: Page Title
description: Brief description
nav: true
nav_order: 5
---
```

3. Add the page content in Markdown format below the front matter

### Page Front Matter Options

- `layout`: Page layout (usually "page")
- `permalink`: URL path for the page
- `title`: Page title
- `description`: Brief description
- `nav`: Set to true to include in navigation menu
- `nav_order`: Position in the navigation menu
- `dropdown`: Optional, set to true for dropdown menus

### Updating Existing Pages

1. Find the page file in the `_pages/` directory
2. Edit the front matter or content as needed
3. Save the file

## Using Markdown

The website uses Markdown for content formatting. Here are some common formatting options:

```markdown
# Heading 1

## Heading 2

### Heading 3

**Bold text**
_Italic text_

[Link text](URL)

![Image description](image-path)

- Bullet point
- Another bullet point

1. Numbered item
2. Another numbered item

> Blockquote

`Inline code`

`code block`
```

For more advanced formatting, consult the [Markdown Guide](https://www.markdownguide.org/).
