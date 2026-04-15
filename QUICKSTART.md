# Quick Start Guide

## Installation Check

Verify all dependencies are installed:
```bash
python convert_problem_sets.py --dry-run
```

You should see: `INFO: All required tools available`

## Common Use Cases

### 1. Convert Everything
```bash
python convert_problem_sets.py
```

This will:
- Find all `.Rmd`, `.md`, `.tex`, `.ipynb`, and `.org` files
- Convert each to LaTeX (if needed), PDF, and HTML
- Report successes and failures at the end

### 2. Test First (Recommended)
```bash
# See what would be converted without doing anything
python convert_problem_sets.py --dry-run

# Test on a single file
python convert_problem_sets.py --pattern "stats/stat581_fa2021/hw1/hw1.Rmd"
```

### 3. Convert Specific Files
```bash
# All homework in stat581
python convert_problem_sets.py --pattern "stats/stat581_fa2021/hw*/*.Rmd"

# All exams
python convert_problem_sets.py --pattern "stats/*/exam*/*.Rmd"

# Everything in a specific course
python convert_problem_sets.py --pattern "stats/stat581_fa2021/**/*.Rmd"
```

### 4. Customize HTML Output
```bash
# Use dark theme
python convert_problem_sets.py --html-theme dark

# Minimal theme with custom components
python convert_problem_sets.py --html-theme minimal --html-components "toc,equation-numbers"

# Full-featured HTML
python convert_problem_sets.py --html-components "floating-toc,search,reading-time,equation-numbers,copy-code,back-to-top,theme-toggle"
```

## What Gets Generated?

For each source file, you get:
- **`.tex`** - LaTeX source (if converted from .Rmd, .md, etc.)
- **`.pdf`** - PDF output via pdflatex
- **`.html`** - Beautiful HTML5 with interactive features

Example:
```
stats/stat581_fa2021/hw1/
├── hw1.Rmd          (original)
├── hw1.tex          (generated)
├── hw1.pdf          (generated)
└── hw1.html         (generated)
```

## Understanding Output

### Success
```
============================================================
Processing: stats/stat581_fa2021/hw1/hw1.Rmd
============================================================
Converting hw1.Rmd to LaTeX...
  ✓ Generated hw1.tex
Converting hw1.tex to PDF...
  ✓ Generated hw1.pdf
Converting hw1.tex to HTML...
  ✓ Generated hw1.html
✓ Successfully converted hw1.Rmd to PDF and HTML
```

### Failure
If conversion fails, you'll see:
```
✗ Failed to generate .tex from hw1.Rmd: <error message>
```

Use `--verbose` to see detailed error messages:
```bash
python convert_problem_sets.py --verbose --pattern "path/to/failing/file.Rmd"
```

## Summary Report

At the end, you get a summary:
```
============================================================
CONVERSION SUMMARY
============================================================
✓ Successes: 75
✗ Failures:  5
⊘ Skipped:   3
============================================================
```

Failed files are listed with reasons for manual investigation.

## Troubleshooting

### Missing R Packages
```r
# In R console
install.packages("knitr")
install.packages("rmarkdown")
```

### LaTeX Errors
Check the error message with `--verbose`:
```bash
python convert_problem_sets.py --verbose --pattern "failing_file.Rmd"
```

Common issues:
- Missing LaTeX packages (install via `tlmgr`)
- Custom `.sty` files not in path
- Syntax errors in LaTeX code

### Test Manually
If a file fails, try converting it manually to diagnose:
```bash
cd stats/stat581_fa2021/hw1
Rscript -e "knitr::knit('hw1.Rmd', output='hw1.tex')"
pdflatex hw1.tex
tex2any hw1.tex --theme academic
```

## Next Steps

1. **Dry run on everything**: `python convert_problem_sets.py --dry-run`
2. **Test on one file**: `python convert_problem_sets.py --pattern "stats/stat581_fa2021/hw1/hw1.Rmd"`
3. **Convert a course**: `python convert_problem_sets.py --pattern "stats/stat581_fa2021/**/*.Rmd"`
4. **Convert everything**: `python convert_problem_sets.py`

## Advanced Options

See `CONVERSION_README.md` for:
- Custom themes and components
- Batch processing strategies
- CI/CD integration
- Selective conversion based on modification time

## Getting Help

```bash
python convert_problem_sets.py --help
```

View available themes and components:
```bash
tex2any --list-themes
tex2any --list-components
```
