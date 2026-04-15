# Automated Problem Set Conversion Workflow

This repository contains tools to automatically convert problem sets from various source formats (R Markdown, Markdown, Jupyter notebooks, etc.) to LaTeX, PDF, and beautiful HTML.

## 🚀 Quick Start

### 1. Check Dependencies
```bash
./check_dependencies.sh
```

This will verify all required tools are installed. If anything is missing, it will provide installation instructions.

### 2. Test on One File
```bash
./convert.sh test "stats/stat581_fa2021/hw1/hw1.Rmd"
```

### 3. Preview What Would Be Converted
```bash
./convert.sh dry-run
```

### 4. Convert Everything
```bash
./convert.sh all
```

## 📁 Files in This Repository

- **`convert_problem_sets.py`** - Main conversion script (Python)
- **`convert.sh`** - Convenient bash wrapper for common tasks
- **`check_dependencies.sh`** - Verify all dependencies are installed
- **`QUICKSTART.md`** - Quick start guide with examples
- **`CONVERSION_README.md`** - Full documentation and troubleshooting
- **`README_CONVERSION.md`** - This file

## 🔧 What It Does

The conversion workflow:

```
Source File (.Rmd, .md, .ipynb, .org, .tex)
    ↓
LaTeX (.tex) ← Generated if needed
    ↓
    ├→ PDF (via pdflatex)
    └→ HTML5 (via tex2any with themes and components)
```

### Supported Input Formats

- **`.Rmd`** - R Markdown (converted via R knitr)
- **`.md`** - Markdown (converted via pandoc)
- **`.ipynb`** - Jupyter notebooks (converted via nbconvert)
- **`.org`** - Org-mode (converted via pandoc)
- **`.tex`** - LaTeX (used directly)

### Generated Outputs

For each source file, you get:
- **PDF** - Professional document via pdflatex
- **HTML** - Beautiful, interactive HTML5 with:
  - Floating table of contents
  - Equation numbering
  - Code copy buttons
  - Back-to-top button
  - Responsive design
  - Multiple theme options

## 💡 Common Usage Patterns

### Convert by Course
```bash
# All stat581 assignments
./convert.sh course "stats/stat581_fa2021/**/*.Rmd"

# All homework across all courses
./convert.sh course "stats/*/hw*/*.Rmd"

# All exams
./convert.sh course "stats/*/exam*/*.Rmd"
```

### Customize HTML Output
```bash
# Dark theme
python convert_problem_sets.py --html-theme dark

# Minimal theme with specific components
python convert_problem_sets.py --html-theme minimal \
    --html-components "toc,equation-numbers,reading-time"

# Full-featured output
python convert_problem_sets.py \
    --html-theme academic \
    --html-components "floating-toc,search,reading-time,equation-numbers,copy-code,back-to-top,theme-toggle,reading-progress"
```

### Available Themes
- **academic** - Beautiful, minimalistic (default)
- **clean** - Clean minimal theme
- **dark** - Dark mode
- **minimal** - Ultra-minimal
- **serif** - Classic serif typography
- **modern** - Modern with generous whitespace

See all components: `tex2any --list-components`

## 🔍 Features

✅ **Batch Processing** - Convert entire directories at once
✅ **Smart Filtering** - Exclude hidden files and directories automatically
✅ **Pattern Matching** - Use glob patterns to select specific files
✅ **Dry Run Mode** - Preview without making changes
✅ **Error Handling** - Detailed reports of successes and failures
✅ **Customizable HTML** - Multiple themes and interactive components
✅ **Parallel Execution** - Fast conversion of multiple files
✅ **Progress Tracking** - Clear status for each file

## 📊 Example Output

```
============================================================
CONVERSION SUMMARY
============================================================
✓ Successes: 75
✗ Failures:  5
⊘ Skipped:   3
============================================================

Failed conversions:
  ✗ stats/course1/hw1/hw1.Rmd: Failed to convert to .tex
  ...
```

## 🛠️ Troubleshooting

### Check Dependencies First
```bash
./check_dependencies.sh
```

### Common Issues

#### 1. Missing R Packages
```r
install.packages(c("knitr", "rmarkdown", "readxl", "printr"))
```

#### 2. LaTeX Errors
- Ensure all required LaTeX packages are installed
- Check for custom `.sty` files in the document
- Use `--verbose` to see detailed error messages

#### 3. Test Individual Files
```bash
./convert.sh test "path/to/problematic/file.Rmd"
```

See `CONVERSION_README.md` for detailed troubleshooting.

## 📚 Documentation

- **`QUICKSTART.md`** - Start here! Quick examples and common use cases
- **`CONVERSION_README.md`** - Complete documentation with:
  - Detailed conversion logic for each format
  - Advanced usage examples
  - Comprehensive troubleshooting guide
  - CI/CD integration tips

## 🎯 Design Principles

1. **Minimal Manual Intervention** - Automated as much as possible
2. **Informative Errors** - When something fails, tell the user why
3. **Flexible** - Support multiple input formats and output customization
4. **Safe** - Dry-run mode and confirmation for bulk operations
5. **Fast** - Efficient batch processing

## 🔒 Safety Features

- **Hidden files excluded** - Won't process `.git/` or other hidden directories
- **Dry-run mode** - Test without making changes
- **Confirmation prompts** - For bulk operations via `convert.sh all`
- **Detailed logging** - Track what's happening with `--verbose`

## 🤝 Contributing

Found a bug or want to add support for another format? The main script is `convert_problem_sets.py`. Key areas:

- **New format support** - Add conversion function in `ProblemSetConverter` class
- **Better error handling** - Improve error messages in `run_command()`
- **HTML customization** - Extend `tex_to_html()` method

## 📝 Examples

See `QUICKSTART.md` for many more examples!

### Basic Workflow
```bash
# 1. Check everything is installed
./check_dependencies.sh

# 2. See what would be converted
./convert.sh dry-run

# 3. Test on one file
./convert.sh test "stats/stat581_fa2021/hw1/hw1.Rmd"

# 4. Convert a course
./convert.sh course "stats/stat581_fa2021/**/*.Rmd"

# 5. Review output
ls stats/stat581_fa2021/hw1/
# hw1.Rmd  hw1.tex  hw1.pdf  hw1.html
```

## 🎨 HTML Output Examples

The generated HTML includes:
- Responsive design that works on mobile
- Syntax highlighting for code blocks
- Beautiful math rendering
- Interactive table of contents
- Dark/light theme support (if enabled)
- Copy buttons for code blocks
- Reading time estimates (if enabled)

Open any `.html` file in your browser to see the results!

## 📞 Getting Help

```bash
# Script help
python convert_problem_sets.py --help
./convert.sh help

# Check what tex2any can do
tex2any --list-themes
tex2any --list-components
tex2any --help
```

---

**Ready to get started?**
Run `./check_dependencies.sh` and then check out `QUICKSTART.md`!
