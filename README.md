# 🏃‍♂️ Digital Athlete Lab Website 🧬

This repository contains the source code for the [Digital Athlete Lab](https://rjholash.github.io) website, the research lab of Dr. R. John Holash at the University of Calgary's Faculty of Kinesiology.

## 🔬 About the Lab

The Digital Athlete Lab focuses on cutting-edge research in muscle physiology and the transformative power of exercise on the human body. Our work investigates the complex mechanisms through which physical activity influences health, well-being, and the aging process.

## 📚 Website Content

This website showcases:

- 🔍 **Research Projects** - Innovative findings from the Digital Athlete Lab
- 📝 **Publications** - Scholarly work by Dr. Holash and lab members
- 🎓 **Teaching Resources** - Materials related to exercise physiology and muscle science
- 🧰 **Open-source Tools** - Repositories and resources for exercise science research
- 📰 **News & Updates** - Latest activities and achievements from our lab

## 📋 Website Maintenance Documentation

Comprehensive documentation for maintaining this website is available in the [docs](docs/) directory:

- [Website Structure](docs/structure.md) - Overview of site organization
- [Content Management](docs/content-management.md) - How to update CV, projects, and other content
- [Publication Management](docs/publication-management/) - Cross-platform tools for publication updates
- [Deployment Guide](docs/deployment.md) - How to test and deploy the website

### 📄 CV Management System

The CV page is managed through a two-file system that separates content from presentation:

**Main Files:**
- `_pages/cv.md` - CV page template with layout settings and metadata
- `_data/cv.yml` - Structured YAML file containing all CV content

**How It Works:**
The CV page uses Jekyll's data file system where the `cv.md` template references the `layout: cv` and the actual content is dynamically loaded from `cv.yml`. This approach provides several advantages:

- **Easy Content Updates**: Modify CV information in the structured YAML format without touching HTML/Markdown
- **Consistent Formatting**: The layout template ensures uniform presentation across all CV sections
- **Version Control**: Track changes to CV content through git history
- **Maintainability**: Separate content from presentation logic

**To Update Your CV:**
1. **Content Changes**: Edit `_data/cv.yml` - add/modify sections like Education, Experience, Publications
2. **Layout Changes**: Modify `_layouts/cv.html` (if it exists) or page settings in `_pages/cv.md`
3. **PDF Version**: Update the `cv_pdf` field in `_pages/cv.md` to reference your latest PDF file

**YAML Structure Example:**
```yaml
- title: Section Name
  type: time_table  # or 'map' for key-value pairs
  contents:
    - title: Position/Degree
      institution: Institution Name
      year: Date Range
      description:
        - Bullet point description
        - Additional details
```

**Backup Files:**
- `cv_bak.yml` - Backup version of CV data
- `_data/cv_old.yml` - Previous version for reference

## ⚙️ Technical Details

This website is built using:

- 💎 [Jekyll](https://jekyllrb.com/) - A powerful static site generator
- 🎨 [al-folio](https://github.com/alshedivat/al-folio) - A clean, responsive Jekyll theme for academics
- 🚀 [GitHub Pages](https://pages.github.com/) - Seamless hosting integrated with GitHub repositories

## 📫 Contact

For more information about the Digital Athlete Lab, visit our website at [https://rjholash.github.io](https://rjholash.github.io) or contact:

**Dr. R. John Holash**  
Faculty of Kinesiology  
Human Performance Laboratory  
University of Calgary  
2500 University Drive  
Calgary, AB T2N 1N4  
✉️ Email: rjholash@ucalgary.ca

---

> _"The future is faster than you think!"_ 💭
