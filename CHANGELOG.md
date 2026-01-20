# AI Boot Camp - Change Log

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


