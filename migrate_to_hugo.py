#!/usr/bin/env python3
"""
Migrate problem sets from this repository to the metafunctor Hugo blog.

This script:
1. Converts .Rmd files to .md using knitr::knit()
2. Replaces front matter with Hugo-compatible YAML
3. Copies markdown and assets to metafunctor/content/probsets/

Usage:
    python migrate_to_hugo.py [--dry-run] [--course COURSE] [--assignment ASSIGNMENT]

Examples:
    # Migrate all of stat581
    python migrate_to_hugo.py --course stat581

    # Migrate specific assignment
    python migrate_to_hugo.py --course stat581 --assignment hw1

    # Dry run to see what would be done
    python migrate_to_hugo.py --course stat581 --dry-run
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List

# Configuration
PROBLEM_SETS_ROOT = Path(__file__).parent
METAFUNCTOR_ROOT = Path.home() / "github" / "repos" / "metafunctor"
PROBSETS_CONTENT = METAFUNCTOR_ROOT / "content" / "probsets"

# Course metadata
COURSE_INFO = {
    "stat478": {
        "name": "Time Series Analysis",
        "semester": "Spring 2021",
        "instructor": "Dr. Beidi",
        "tags": ["statistics", "time-series", "R", "SIUe"],
        "source_dir": "stat478_time_series_analysis_sp2021",
    },
    "stat482": {
        "name": "Regression Analysis",
        "semester": "Fall 2021",
        "instructor": "Dr. Andrew Neath",
        "tags": ["statistics", "regression-analysis", "R", "SIUe"],
        "source_dir": "stat482_regression_analysis_fa2021",
    },
    "stat575": {
        "name": "Computational Statistics",
        "semester": "Summer 2021",
        "instructor": "Dr. Qiang Beidi",
        "tags": ["statistics", "computational-statistics", "R", "SIUe"],
        "source_dir": "stat575_su2021",
    },
    "stat579": {
        "name": "Discrete Multivariate Analysis",
        "semester": "Spring 2021",
        "instructor": "Dr. Beidi",
        "tags": ["statistics", "multivariate-analysis", "categorical-data", "R", "SIUe"],
        "source_dir": "stat579_discrete_multivariate_analysis_sp2021",
    },
    "stat581": {
        "name": "Statistical Methods",
        "semester": "Fall 2021",
        "instructor": "Dr. Neath",
        "tags": ["statistics", "statistical-methods", "R", "SIUe"],
        "source_dir": "stat581_fa2021",
    },
}


def get_semester_date(semester: str) -> str:
    """Convert semester string to approximate date."""
    semester_lower = semester.lower()
    if "spring 2021" in semester_lower:
        return "2021-05-01"
    elif "summer 2021" in semester_lower:
        return "2021-08-01"
    elif "fall 2021" in semester_lower:
        return "2021-12-01"
    elif "fall 2022" in semester_lower:
        return "2022-12-01"
    return "2021-01-01"


def assignment_to_title(assignment: str, course_code: str, course_name: str) -> str:
    """Convert assignment directory name to human-readable title."""
    # Handle special cases
    if assignment.startswith("hw"):
        num = assignment.replace("hw", "").replace("_", " ").replace(".", " ")
        return f"{course_name} - STAT {course_code[4:]} - Problem Set {num.strip()}"
    elif assignment.startswith("exam"):
        num = assignment.replace("exam", "").replace("_", " ")
        return f"{course_name} - STAT {course_code[4:]} - Exam {num.strip()}"
    elif assignment == "final_exam":
        return f"{course_name} - STAT {course_code[4:]} - Final Exam"
    elif assignment == "project":
        return f"{course_name} - STAT {course_code[4:]} - Project"
    return f"{course_name} - STAT {course_code[4:]} - {assignment}"


def assignment_to_slug(course_code: str, assignment: str) -> str:
    """Generate URL slug for assignment."""
    clean_assignment = assignment.replace(".", "-").replace("_", "-")
    return f"{course_code}-{clean_assignment}"


def cleanup_pandoc_markdown(content: str) -> str:
    """Clean up pandoc-generated markdown for Hugo compatibility."""
    import re

    # Remove pandoc div wrappers
    content = re.sub(r'::: \{[^}]*\}\n?', '', content)
    content = re.sub(r':::\n?', '', content)

    # Remove title block header content
    content = re.sub(r'# [^{]+\{[^}]*\.title[^}]*\}\n*', '', content)

    # Convert display math spans: [\$$...\$$]{.math .display} -> $$...$$
    content = re.sub(r'\[\\\$\$([^\]]+)\\\$\$\]\{\.math \.display\}', r'$$\1$$', content)

    # Convert inline math: $...\$ -> $...$
    content = re.sub(r'\$([^$]+)\\\$', r'$\1$', content)

    # Remove bold markers around function names in code (pandoc artifact)
    content = re.sub(r'\*\*([a-zA-Z_][a-zA-Z0-9_]*)\*\*', r'\1', content)

    # Fix escaped characters in code
    content = content.replace('\\<-', '<-')
    content = content.replace('\\[', '[')
    content = content.replace('\\]', ']')
    content = content.replace('\\*', '*')

    # Clean up extra newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Fix code block formatting - remove space before code output
    content = re.sub(r'```r\n([^`]+)\n\n    ##', r'```r\n\1\n```\n\n```\n##', content)

    # Remove author line that duplicates front matter
    content = re.sub(r'^Alex Towell \(\[`[^`]+`\]\([^)]+\)\)\n+', '', content, flags=re.MULTILINE)

    return content


def convert_html_to_md(html_path: Path, output_path: Path, dry_run: bool = False) -> bool:
    """Convert .html to .md using pandoc."""
    if dry_run:
        print(f"  [DRY RUN] Would convert {html_path.name} to markdown via pandoc")
        return True

    try:
        result = subprocess.run(
            ["pandoc", str(html_path), "-f", "html", "-t", "markdown",
             "--wrap=none", "-o", str(output_path)],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            print(f"  ERROR: pandoc failed for {html_path.name}")
            print(f"  {result.stderr[:300]}")
            return False

        # Clean up the generated markdown
        if output_path.exists():
            content = output_path.read_text()
            content = cleanup_pandoc_markdown(content)
            output_path.write_text(content)

        return output_path.exists()

    except Exception as e:
        print(f"  ERROR converting HTML: {e}")
        return False


def convert_rmd_to_md(rmd_path: Path, output_path: Path, dry_run: bool = False) -> bool:
    """Convert .Rmd to .md using knitr::knit()."""
    if dry_run:
        print(f"  [DRY RUN] Would convert {rmd_path.name} to markdown")
        return True

    # Create R script to run knit
    r_script = f"""
setwd("{rmd_path.parent}")
library(knitr)
knit("{rmd_path.name}", output="{output_path.name}", quiet=TRUE)
"""

    try:
        result = subprocess.run(
            ["Rscript", "-e", r_script],
            cwd=rmd_path.parent,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )

        if result.returncode != 0:
            print(f"  ERROR: knitr failed for {rmd_path.name}")
            print(f"  {result.stderr[:500]}")
            return False

        return output_path.exists()

    except subprocess.TimeoutExpired:
        print(f"  ERROR: Timeout converting {rmd_path.name}")
        return False
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def extract_summary_from_rmd(rmd_path: Path) -> str:
    """Extract a summary from the Rmd content (first paragraph or description)."""
    try:
        content = rmd_path.read_text()

        # Try to find content after YAML front matter
        parts = content.split("---", 2)
        if len(parts) >= 3:
            body = parts[2].strip()

            # Get first non-code paragraph that doesn't contain LaTeX
            lines = []
            in_code = False
            for line in body.split("\n"):
                if line.startswith("```"):
                    in_code = not in_code
                    continue
                # Skip LaTeX commands, code blocks, and headers
                if not in_code and line.strip():
                    if line.startswith("#"):
                        continue
                    if line.startswith("\\"):  # Skip LaTeX commands
                        continue
                    if "$" in line or "\\" in line:  # Skip lines with math
                        continue
                    lines.append(line.strip())
                    if len(" ".join(lines)) > 100:
                        break

            if lines:
                summary = " ".join(lines)[:200]
                # Clean any remaining problematic characters
                summary = summary.replace("\\", "").replace("$", "")
                if len(summary) == 200:
                    summary = summary[:summary.rfind(" ")] + "..."
                if summary:
                    return summary

    except Exception:
        pass

    return "Problem set solutions and analysis."


def create_hugo_front_matter(
    title: str,
    slug: str,
    date: str,
    summary: str,
    tags: List[str],
    author: str = "Alex Towell"
) -> str:
    """Create Hugo-compatible YAML front matter."""
    tags_yaml = "\n".join(f"- {tag}" for tag in tags)

    return f"""---
title: "{title}"
author: "{author} (lex@metafunctor.com)"
date: '{date}'
slug: {slug}
summary: "{summary}"
tags:
{tags_yaml}
---

"""


def replace_front_matter(md_content: str, new_front_matter: str) -> str:
    """Replace existing YAML front matter with Hugo-compatible version."""
    # Remove existing front matter
    if md_content.startswith("---"):
        parts = md_content.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]
        else:
            body = md_content
    else:
        body = md_content

    return new_front_matter + body.lstrip()


def find_assets(source_dir: Path) -> List[Path]:
    """Find all asset files (images, data, R scripts) in directory."""
    asset_patterns = ["*.png", "*.jpg", "*.jpeg", "*.gif", "*.pdf", "*.csv",
                      "*.txt", "*.xlsx", "*.xls", "*.R", "*.r", "*.RData"]
    assets = []

    for pattern in asset_patterns:
        assets.extend(source_dir.glob(pattern))
        # Also check figure subdirectory
        assets.extend(source_dir.glob(f"figure/{pattern}"))
        assets.extend(source_dir.glob(f"*_files/**/{pattern}"))

    return assets


def migrate_assignment(
    course_code: str,
    assignment: str,
    source_dir: Path,
    dry_run: bool = False
) -> bool:
    """Migrate a single assignment to Hugo."""
    course_info = COURSE_INFO[course_code]

    # Find the main .Rmd file
    rmd_files = list(source_dir.glob("*.Rmd"))

    # Filter out blank/output variants, prefer main file
    main_rmd = None
    for rmd in rmd_files:
        name = rmd.stem.lower()
        if "blank" in name or "output" in name or "backup" in name:
            continue
        if name == assignment or name.startswith(assignment.replace(".", "")):
            main_rmd = rmd
            break

    if not main_rmd and rmd_files:
        # Just use first non-blank file
        for rmd in rmd_files:
            if "blank" not in rmd.stem.lower():
                main_rmd = rmd
                break

    if not main_rmd:
        print(f"  No suitable .Rmd file found in {source_dir}")
        return False

    print(f"  Processing: {main_rmd.name}")

    # Determine output directory
    hugo_assignment_name = assignment.replace(".", "_").replace("-", "_")
    if hugo_assignment_name.startswith("hw"):
        hugo_assignment_name = "problem_set_" + hugo_assignment_name[2:]

    dest_dir = PROBSETS_CONTENT / course_code / hugo_assignment_name

    if dry_run:
        print(f"  [DRY RUN] Would create: {dest_dir}")
    else:
        dest_dir.mkdir(parents=True, exist_ok=True)

    # Try to get markdown content from various sources (in order of preference)
    md_content = None

    # 1. Try HTML file first (most reliable - has rendered R output)
    html_file = source_dir / f"{main_rmd.stem}.html"
    temp_md = source_dir / f"{main_rmd.stem}.converted.md"

    if html_file.exists():
        print(f"  Found HTML file: {html_file.name}")
        if convert_html_to_md(html_file, temp_md, dry_run):
            if not dry_run and temp_md.exists():
                md_content = temp_md.read_text()
                print(f"  Converted HTML to markdown")

    # 2. Fall back to existing .knit.md
    if md_content is None:
        existing_knit_md = source_dir / f"{main_rmd.stem}.knit.md"
        if existing_knit_md.exists():
            print(f"  Using existing {existing_knit_md.name}")
            if not dry_run:
                md_content = existing_knit_md.read_text()

    # 3. Try running knitr (may fail if R environment not set up)
    if md_content is None:
        knitr_output = source_dir / f"{main_rmd.stem}.knit.md"
        if convert_rmd_to_md(main_rmd, knitr_output, dry_run):
            if not dry_run and knitr_output.exists():
                md_content = knitr_output.read_text()

    if md_content is None and not dry_run:
        print(f"  No markdown content available for {main_rmd.name}")
        return False

    if dry_run:
        md_content = "# Placeholder content"

    # Create Hugo front matter
    title = assignment_to_title(assignment, course_code, course_info["name"])
    slug = assignment_to_slug(course_code, assignment)
    date = get_semester_date(course_info["semester"])
    summary = extract_summary_from_rmd(main_rmd)

    new_front_matter = create_hugo_front_matter(
        title=title,
        slug=slug,
        date=date,
        summary=summary,
        tags=course_info["tags"]
    )

    # Replace front matter
    final_content = replace_front_matter(md_content, new_front_matter)

    # Write index.md
    index_path = dest_dir / "index.md"
    if dry_run:
        print(f"  [DRY RUN] Would write: {index_path}")
    else:
        index_path.write_text(final_content)
        print(f"  Created: {index_path}")

    # Copy assets
    assets = find_assets(source_dir)
    for asset in assets:
        rel_path = asset.relative_to(source_dir)
        dest_asset = dest_dir / rel_path

        if dry_run:
            print(f"  [DRY RUN] Would copy: {asset.name}")
        else:
            dest_asset.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(asset, dest_asset)
            print(f"  Copied: {rel_path}")

    return True


def create_course_index(course_code: str, dry_run: bool = False) -> bool:
    """Create or update course _index.md file."""
    course_info = COURSE_INFO[course_code]

    dest_dir = PROBSETS_CONTENT / course_code
    index_path = dest_dir / "_index.md"

    if index_path.exists():
        print(f"  Course index already exists: {index_path}")
        return True

    tags_yaml = "\n".join(f"- {tag}" for tag in course_info["tags"])

    content = f"""---
title: "STAT {course_code[4:]} - {course_info['name']} - SIUe - {course_info['semester']}"
author: Alex Towell
email: lex@metafunctor.com
summary: "Problem sets and solutions for STAT {course_code[4:]} - {course_info['name']} at SIUe."
description: "Problem sets for STAT {course_code[4:]} - {course_info['name']} at SIUe, taught by {course_info['instructor']} during {course_info['semester']}."
date: "{get_semester_date(course_info['semester'])}"
layout: "course"
tags:
{tags_yaml}
---

These problem sets were given by {course_info['instructor']}, a professor in the Department of
Mathematics and Statistics at Southern Illinois University Edwardsville (SIUe)
during {course_info['semester']}.
"""

    if dry_run:
        print(f"  [DRY RUN] Would create course index: {index_path}")
    else:
        dest_dir.mkdir(parents=True, exist_ok=True)
        index_path.write_text(content)
        print(f"  Created course index: {index_path}")

    return True


def get_assignments(course_code: str) -> List[str]:
    """Get list of assignments for a course."""
    course_info = COURSE_INFO[course_code]
    source_dir = PROBLEM_SETS_ROOT / "stats" / course_info["source_dir"]

    assignments = []
    for item in source_dir.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            # Skip backup directories
            if "backup" in item.name.lower():
                continue
            # Check if it has .Rmd files
            if list(item.glob("*.Rmd")):
                assignments.append(item.name)

    return sorted(assignments)


def migrate_course(course_code: str, dry_run: bool = False) -> None:
    """Migrate all assignments for a course."""
    course_info = COURSE_INFO[course_code]
    source_base = PROBLEM_SETS_ROOT / "stats" / course_info["source_dir"]

    print(f"\n{'='*60}")
    print(f"Migrating: {course_code} - {course_info['name']}")
    print(f"{'='*60}")

    # Create course index
    create_course_index(course_code, dry_run)

    # Get and migrate assignments
    assignments = get_assignments(course_code)
    print(f"Found {len(assignments)} assignments: {', '.join(assignments)}")

    for assignment in assignments:
        print(f"\n--- {assignment} ---")
        source_dir = source_base / assignment
        migrate_assignment(course_code, assignment, source_dir, dry_run)


def main():
    parser = argparse.ArgumentParser(
        description="Migrate problem sets to metafunctor Hugo blog"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )
    parser.add_argument(
        "--course",
        choices=list(COURSE_INFO.keys()),
        help="Migrate specific course (default: all new courses)"
    )
    parser.add_argument(
        "--assignment",
        help="Migrate specific assignment within course"
    )
    parser.add_argument(
        "--list-courses",
        action="store_true",
        help="List available courses and exit"
    )
    parser.add_argument(
        "--list-assignments",
        help="List assignments for a course and exit"
    )

    args = parser.parse_args()

    if args.list_courses:
        print("Available courses:")
        for code, info in COURSE_INFO.items():
            print(f"  {code}: {info['name']} ({info['semester']})")
        return

    if args.list_assignments:
        assignments = get_assignments(args.list_assignments)
        print(f"Assignments for {args.list_assignments}:")
        for a in assignments:
            print(f"  {a}")
        return

    if args.assignment and not args.course:
        print("ERROR: --assignment requires --course")
        sys.exit(1)

    if args.course and args.assignment:
        # Migrate single assignment
        course_info = COURSE_INFO[args.course]
        source_dir = PROBLEM_SETS_ROOT / "stats" / course_info["source_dir"] / args.assignment

        if not source_dir.exists():
            print(f"ERROR: Assignment directory not found: {source_dir}")
            sys.exit(1)

        create_course_index(args.course, args.dry_run)
        migrate_assignment(args.course, args.assignment, source_dir, args.dry_run)

    elif args.course:
        # Migrate entire course
        migrate_course(args.course, args.dry_run)

    else:
        # Migrate all courses not yet present
        print("Migrating all courses...")
        for course_code in ["stat478", "stat579", "stat581"]:
            migrate_course(course_code, args.dry_run)

        # Note: stat482 and stat575 already have partial content
        print("\nNote: stat482 and stat575 already have partial content.")
        print("Use --course stat482 or --course stat575 to add remaining assignments.")

    print("\n" + "="*60)
    print("Migration complete!")
    print("="*60)
    print(f"\nTo verify, run: cd {METAFUNCTOR_ROOT} && hugo server")


if __name__ == "__main__":
    main()
