# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A collection of statistics coursework (problem sets, exams, projects) from SIUe graduate courses with automated conversion infrastructure. The goal is to convert R Markdown and other source files to multiple output formats (PDF, HTML, LaTeX) and ultimately publish select content to the metafunctor Hugo blog.

## Courses Included

| Course | Name | Semester | Content |
|--------|------|----------|---------|
| stat478 | Time Series Analysis | Spring 2021 | 11 dirs (hw, exams, project) |
| stat482 | Regression Analysis | Fall 2021 | 17 dirs (hw1-hw13, exams, hw8.book) |
| stat575 | Computational Statistics | Summer 2021 | 10 dirs (hw1-hw4, exams) |
| stat579 | Discrete Multivariate Analysis | Spring 2021 | 15 dirs (hw1-hw10, exams) |
| stat581 | (Statistical Methods) | Fall 2021 | 15 dirs (hw1-hw11, exams) |

## Conversion Commands

Three entry points exist. Use `convert.sh` for one-off tasks, `convert_problem_sets.py` for full control, and `migrate_to_hugo.py` for publishing.

```bash
# Verify toolchain (pdflatex, tex2any, pandoc, Rscript + knitr/rmarkdown)
./check_dependencies.sh

# Wrapper shortcuts (dry-run, test one file, convert by course, convert all)
./convert.sh dry-run
./convert.sh test "stats/stat581_fa2021/hw1/hw1.Rmd"
./convert.sh course "stats/stat581_fa2021/**/*.Rmd"
./convert.sh all

# Direct invocation of the main script
python convert_problem_sets.py --dry-run
python convert_problem_sets.py --pattern "stats/stat581_fa2021/hw1/hw1.Rmd"
python convert_problem_sets.py --verbose --pattern "path/to/file.Rmd"

# HTML customization (themes: academic, clean, dark, minimal, serif, modern)
python convert_problem_sets.py --html-theme dark
python convert_problem_sets.py --html-components "floating-toc,search,reading-time"
```

### Manual Conversion (debugging)
```bash
cd stats/stat581_fa2021/hw1
Rscript -e "knitr::knit('hw1.Rmd', output='hw1.tex')"
pdflatex hw1.tex
tex2any hw1.tex --theme academic
```

## File Organization

```
stats/
└── stat{course}_{semester}/
    ├── hw{N}/
    │   ├── hw{N}.Rmd          # Source
    │   ├── hw{N}.tex          # Generated
    │   ├── hw{N}.pdf          # Generated
    │   ├── hw{N}.html         # Generated
    │   └── data files, figures, etc.
    ├── exam{N}/
    └── project/
```

## Hugo Blog Integration (metafunctor)

### Existing Problem Sets Section
The metafunctor blog at `~/github/repos/metafunctor` already has:
- **URL**: `https://metafunctor.com/probsets/`
- **Content location**: `/content/probsets/`
- **Existing courses**: stat575 (4 problem sets), stat482 (1 problem set)
- **Layout**: Uses `layout: "course"` for course index pages

### Adding New Problem Sets to Hugo

1. **Course index** (`/content/probsets/stat{XXX}/_index.md`):
```yaml
---
title: "STAT XXX - Course Name - SIUe - Semester Year"
author: Alex Towell
summary: "Problem sets and solutions for STAT XXX"
date: "2021-08-01"
layout: "course"
tags:
  - statistics
  - course-topic
  - SIUe
---
```

2. **Individual problem set** (`/content/probsets/stat{XXX}/problem_set_N/index.md`):
```yaml
---
title: "Course Name - STAT XXX - Problem Set N"
author: "Alex Towell"
summary: "Topics covered: ..."
date: "2021-07-10"
tags:
  - statistics
  - specific-topic
---
```

3. **Supporting files**: Place in same directory as `index.md` (figures, data, R scripts)

### Conversion Workflow to Hugo

Use `migrate_to_hugo.py`. It runs `knitr::knit()` on each `.Rmd` to get plain `.md` (not a full render), rewrites the front matter to the Hugo schema per the `COURSE_INFO` dict at the top of the script, and copies markdown + assets to `~/github/repos/metafunctor/content/probsets/stat{XXX}/`.

```bash
python migrate_to_hugo.py --dry-run --course stat581
python migrate_to_hugo.py --course stat581 --assignment hw1
python migrate_to_hugo.py --course stat581
```

When adding a new course, extend `COURSE_INFO` in `migrate_to_hugo.py` (name, semester, instructor, tags, source_dir). That dict is the single source of truth for Hugo metadata.

## Source File Types

| Extension | Description | Conversion Path |
|-----------|-------------|-----------------|
| `.Rmd` | R Markdown | Rmd → tex → pdf; Rmd → html |
| `.md` | Markdown | pandoc → tex → pdf |
| `.tex` | LaTeX | pdflatex → pdf |
| `.ipynb` | Jupyter | nbconvert → tex → pdf |
| `.org` | Org-mode | pandoc → tex → pdf |

## Architecture Notes

- `convert_problem_sets.py`: Main conversion script (`ProblemSetConverter` class). Handles dependency checking, batch processing, and error reporting.
  - `.Rmd` files use `rmarkdown::render()` which generates both PDF and .tex
  - Non-Rmd files skip HTML conversion (tex2any timeout issues)
- `convert.sh`: Thin bash wrapper around the Python script for common tasks (`dry-run`, `test`, `course`, `all`).
- `migrate_to_hugo.py`: Separate pipeline that bypasses PDF/HTML generation, emits plain `.md` with Hugo front matter, and syncs into the metafunctor content tree.
- Conversions run in the source file's directory for relative path resolution.
- R library path (`~/R/library`) is added to the `R_LIBS` environment variable.
- `.gitignore` covers LaTeX build artifacts (`.aux`, `.log`, `.toc`, `.fdb_latexmk`, etc.), so re-running conversions does not pollute commits. PDFs and HTML outputs are currently tracked.
