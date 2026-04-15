# Problem Set Conversion Tool

Automated script to convert problem sets from various formats (Rmd, Markdown, Jupyter, Org-mode) to LaTeX, HTML, and PDF.

## Features

- **Multi-format support**: Converts `.Rmd`, `.md`, `.ipynb`, `.org`, and `.tex` files
- **Automated pipeline**:
  1. Source → LaTeX (if needed)
  2. LaTeX → PDF (using pdflatex)
  3. LaTeX → HTML (using tex2any)
- **Batch processing**: Recursively processes entire directory trees
- **Dry run mode**: Preview what would be converted without making changes
- **Pattern matching**: Filter files using glob patterns
- **Error handling**: Reports successes, failures, and skipped files

## Requirements

The following tools must be installed and available in PATH:

- `pdflatex` - LaTeX to PDF conversion
- `tex2any` - LaTeX to HTML conversion
- `pandoc` - Markdown/Org-mode to LaTeX conversion
- `Rscript` - R Markdown to LaTeX conversion (requires knitr package)

Install missing R packages:
```r
install.packages("knitr")
install.packages("rmarkdown")
```

## Basic Usage

### Convert all files in current directory
```bash
python convert_problem_sets.py
```

### Dry run (see what would be converted)
```bash
python convert_problem_sets.py --dry-run
```

### Convert specific files using patterns
```bash
# Convert all Rmd files in stat581 course
python convert_problem_sets.py --pattern "stats/stat581_fa2021/*/*.Rmd"

# Convert all homework files
python convert_problem_sets.py --pattern "stats/*/hw*/*"

# Convert a single file
python convert_problem_sets.py --pattern "stats/stat581_fa2021/hw1/hw1.Rmd"
```

### Verbose output for debugging
```bash
python convert_problem_sets.py --verbose
```

### Specify custom directory
```bash
python convert_problem_sets.py --dir /path/to/problem/sets
```

### Customize HTML output
```bash
# Use a different theme
python convert_problem_sets.py --html-theme dark

# Add custom components
python convert_problem_sets.py --html-components "floating-toc,search,reading-time,copy-code"

# Available themes: academic, clean, dark, minimal, serif, modern
# See tex2any --list-components for all available components
```

## Conversion Logic

### R Markdown (.Rmd)
1. Uses R `knitr::knit()` to convert to `.tex`
2. Runs pdflatex twice to resolve references
3. Runs tex2any to generate HTML

### Markdown (.md)
1. Uses pandoc with `--standalone` flag to convert to `.tex`
2. Runs pdflatex twice to resolve references
3. Runs tex2any to generate HTML

### Jupyter Notebooks (.ipynb)
1. Uses `jupyter nbconvert --to latex` to convert to `.tex`
2. Runs pdflatex twice to resolve references
3. Runs tex2any to generate HTML

### Org-mode (.org)
1. Uses pandoc to convert to `.tex`
2. Runs pdflatex twice to resolve references
3. Runs tex2any to generate HTML

### LaTeX (.tex)
1. Already in LaTeX format (skips conversion)
2. Runs pdflatex twice to resolve references
3. Runs tex2any with configurable theme and components to generate HTML

**Default HTML Settings:**
- Theme: `academic` (beautiful, minimalistic with excellent readability)
- Components: `floating-toc,equation-numbers,copy-code,back-to-top`

You can customize these with `--html-theme` and `--html-components` flags.

## Output

For each source file, the script generates:
- `filename.tex` (if converted from another format)
- `filename.pdf`
- `filename.html`

All output files are placed in the same directory as the source file.

## Error Handling

The script will:
- **Continue** if individual files fail (reports at end)
- **Skip** unsupported file formats
- **Report** detailed error messages with `--verbose` flag
- **Exit with code 1** if any conversions failed

### Common Issues

#### Missing R packages
```
Error: there is no package called 'knitr'
```
**Solution**: Install required R packages:
```r
install.packages("knitr")
install.packages("rmarkdown")
```

#### LaTeX errors
If pdflatex fails, check:
- Missing LaTeX packages (install via `tlmgr` or package manager)
- Syntax errors in .tex file
- Missing dependencies (e.g., custom .sty files)

#### tex2any errors
Ensure tex2any is installed and in PATH:
```bash
which tex2any
# Should output: /home/spinoza/venv/bin/tex2any
```

## Examples

### Convert all homework assignments
```bash
python convert_problem_sets.py --pattern "stats/*/hw*/*.Rmd"
```

### Test on a single file first
```bash
python convert_problem_sets.py --dry-run --pattern "stats/stat581_fa2021/hw1/hw1.Rmd"
```

### Batch convert with verbose output
```bash
python convert_problem_sets.py --verbose > conversion.log 2>&1
```

### Convert only exam files
```bash
python convert_problem_sets.py --pattern "stats/*/exam*/*.Rmd"
```

## Summary Report

After processing, the script displays:
- ✓ **Successes**: Files fully converted to PDF and HTML
- ✗ **Failures**: Files that encountered errors
- ⊘ **Skipped**: Unsupported file formats

Example output:
```
============================================================
CONVERSION SUMMARY
============================================================
✓ Successes: 75
✗ Failures:  5
⊘ Skipped:   3
============================================================
```

Failed and skipped files are listed with reasons for manual intervention.

## Troubleshooting

### 1. Check dependencies
```bash
python convert_problem_sets.py --dry-run
# First line should say: "All required tools available"
```

### 2. Test single file
```bash
python convert_problem_sets.py --dry-run --verbose --pattern "path/to/file.Rmd"
```

### 3. Review errors
Use `--verbose` flag to see detailed error messages from conversion tools.

### 4. Manual intervention
For files that fail conversion:
1. Check the error message in the summary
2. Examine the source file for issues
3. Try converting manually to diagnose:
   ```bash
   cd stats/stat581_fa2021/hw1
   Rscript -e "knitr::knit('hw1.Rmd', output='hw1.tex')"
   pdflatex hw1.tex
   tex2any hw1.tex
   ```

## Advanced Usage

### Custom conversion for specific files
For files requiring special handling, you can:
1. Add custom conversion functions to the script
2. Use the `--pattern` flag to process them separately
3. Pre-process files manually, then run the script

### Integration with CI/CD
```bash
# In your CI/CD pipeline
python convert_problem_sets.py || echo "Some conversions failed"
```

### Selective conversion
```bash
# Convert only files modified in last 7 days
find . -name "*.Rmd" -mtime -7 | while read f; do
  python convert_problem_sets.py --pattern "$f"
done
```
