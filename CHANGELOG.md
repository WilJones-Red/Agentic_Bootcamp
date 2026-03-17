# AI Boot Camp - Change Log

## March 17, 2026

### Theme Refinements
- Fixed TOC active item text color to use cosmo blue instead of sandstone green
- Added Contributors page under Resources section
- Corrected Warren Buffett image path in Module 6

### Content Updates
- Toned down homepage introduction for more professional tone
- Updated Module 4 subtitle to "Debugging, Tracing, and Evaluating AI Agents"
- Clarified target audience on homepage to mention BYU-I Data Science Society

### Files Modified
- `cosmo-colors.css` - TOC active item styling
- `resources/contributors.qmd` - New empty contributors page
- `modules/module6.qmd` - Fixed image path
- `index.qmd` - Updated intro and target audience
- `modules/module4.qmd` - Updated subtitle

---

## March 10, 2026

### Module 7 Restructure
- Completely rewrote Module 7 to match course formatting standards
- Added comprehensive drift detection content (data drift, concept drift, prediction drift)
- Included real-world examples and discussion questions
- Added coding activity instructions with statistical tests and retraining workflows
- Expanded learning objectives and best practices for production AI

### Files Modified
- `modules/module7.qmd` - Full content restructure

---

## February 28, 2026

### Theme Customization
- Implemented hybrid sandstone/cosmo theme approach
- Created `cosmo-colors.css` for color variable overrides
- Changed global theme from cosmo to sandstone while preserving cosmo colors
- Updated all module files to use sandstone theme consistently
- Maintained sandstone structure with cosmo blue color scheme

### Files Modified
- `_quarto.yml` - Updated theme and CSS files
- `cosmo-colors.css` - New CSS variable override file
- `modules/module1-7.qmd` - Theme declarations updated
- `resources/colabs.qmd` - Theme updated
- `resources/dictionary.qmd` - Theme updated

---

## February 22, 2026

### Sidebar Spacing and Layout
- Added spacing between sidebar navigation items (8px/12px margins)
- Compacted logo and navigation positioning with negative margins
- Moved logo up and reduced space between logo and search bar
- Fine-tuned sidebar layout for cleaner appearance

### Files Modified
- `styles.css` - Sidebar item spacing, logo positioning adjustments

---

## February 8, 2026

### Resource Pages Implementation
- Created comprehensive Notebooks page documenting all 6 Google Colab projects
- Built Reference page with documentation links and 30+ terminology definitions
- Added getting started guides and project descriptions
- Organized documentation by LLM providers, frameworks, and tools
- Hidden TOC on home, notebooks, and reference pages for cleaner layout

### Files Created
- `resources/colabs.qmd` - Notebooks documentation
- `resources/dictionary.qmd` - Reference and terminology

### Files Modified
- `index.qmd` - Added TOC: false
- `_quarto.yml` - Added Resources section to sidebar

---

## January 28, 2026

### Homepage Development
- Created complete landing page with hero section
- Added course overview and learning outcomes
- Built prerequisite list focused on Google Colab (no local Python install)
- Included comprehensive weekly breakdown with descriptions
- Styled all links consistently with bold formatting and arrows

### Files Modified
- `index.qmd` - Complete homepage content

---

## January 25, 2026

### Visual Branding Updates
- Replaced BYUI logo with DS_Logo.png
- Increased logo size from 120px to 250px
- Added background-vector.png at 9% opacity
- Fixed logo CSS selector specificity issue
- Centered logo with proper positioning

### Files Modified
- `_quarto.yml` - Logo path updated
- `styles.css` - Logo sizing and background image styling

---

## January 22, 2026

### Navigation Redesign
- Converted top navbar to left sidebar navigation
- Implemented docked sidebar style with light background
- Added logo to sidebar
- Organized modules and resources in collapsible sections
- Removed top navbar completely

### Files Modified
- `_quarto.yml` - Sidebar navigation configuration
- `styles.css` - Sidebar-specific styling

---

## January 20, 2026

### JupyterLite Integration Improvements
- Updated JupyterLite iframe source from demo site to more stable jupyter.org hosted version
- Removed embedded REPL console due to persistent CSP and Pyodide errors
- Added instructions for using console within JupyterLab (File → New → Console)
- Added documentation on saving/downloading notebooks
- Clarified that notebooks auto-save to browser local storage

### In Progress
- Marimo demo integration - Taking longer than expected due to requirement for locally running server to handle backend operations

### Files Modified
- `modules/jupyterlite-demo.qmd` - Updated iframe sources and added save instructions

---

## January 13, 2026

### Website Setup
- Created Quarto website structure with basic architecture
- Set up navigation bar with Home, Course Modules (1-7), and Resources
- Added BYU-I logo to navbar and as favicon
- Created placeholder pages for all 7 modules

### Styling Changes
- Applied Cosmo theme
- Added custom blue navbar color (#4a90e2)
- Adjusted BYU-I logo size to 90px height
- Added navbar shadow effect

### Files Created
- `_quarto.yml` - Main configuration file
- `index.qmd` - Home page
- `modules/module1.qmd` through `modules/module7.qmd` - Module pages
- `styles.css` - Custom styling

---


