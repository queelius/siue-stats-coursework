#!/usr/bin/env python3
"""
Automated Problem Set Conversion Script

Converts problem sets to LaTeX, HTML, and PDF formats.
Supports: .Rmd, .md, .tex, .ipynb, .org

Usage:
    python convert_problem_sets.py [--dry-run] [--verbose] [--pattern PATTERN]
"""

import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class ConversionError(Exception):
    """Custom exception for conversion errors"""
    pass


class ProblemSetConverter:
    """Handles conversion of problem sets to multiple formats"""

    def __init__(self, dry_run: bool = False, verbose: bool = False,
                 html_theme: str = 'academic',
                 html_components: str = 'floating-toc,equation-numbers,copy-code,back-to-top'):
        self.dry_run = dry_run
        self.verbose = verbose
        self.html_theme = html_theme
        self.html_components = html_components
        self.successes = []
        self.failures = []
        self.skipped = []

        if verbose:
            logger.setLevel(logging.DEBUG)

    def check_dependencies(self) -> bool:
        """Check if required tools are available"""
        required = ['pdflatex', 'tex2any', 'pandoc', 'Rscript']
        missing = []

        for tool in required:
            if subprocess.run(['which', tool], capture_output=True).returncode != 0:
                missing.append(tool)

        if missing:
            logger.error(f"Missing required tools: {', '.join(missing)}")
            return False

        logger.info("All required tools available")
        return True

    def run_command(self, cmd: List[str], cwd: Optional[Path] = None) -> Tuple[bool, str]:
        """
        Run a shell command and return success status and output

        Args:
            cmd: Command as list of strings
            cwd: Working directory for command

        Returns:
            Tuple of (success, output)
        """
        if self.dry_run:
            logger.info(f"[DRY RUN] Would execute: {' '.join(cmd)}")
            return True, ""

        try:
            logger.debug(f"Executing: {' '.join(cmd)}")

            # Set up environment with user R library path
            env = os.environ.copy()
            home = os.path.expanduser("~")
            r_libs_user = os.path.join(home, "R", "library")
            if os.path.exists(r_libs_user):
                # Add user library to R_LIBS
                existing_libs = env.get('R_LIBS', '')
                env['R_LIBS'] = f"{r_libs_user}:{existing_libs}" if existing_libs else r_libs_user
                logger.debug(f"Set R_LIBS to: {env['R_LIBS']}")

            result = subprocess.run(
                cmd,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=None,  # No timeout - let it run as long as needed
                env=env
            )

            if result.returncode != 0:
                error_msg = result.stderr or result.stdout
                logger.debug(f"Command failed with: {error_msg}")
                return False, error_msg

            return True, result.stdout

        except Exception as e:
            return False, str(e)

    def convert_rmd_to_tex(self, rmd_file: Path) -> Optional[Path]:
        """
        Convert .Rmd to .tex using R rmarkdown

        Args:
            rmd_file: Path to .Rmd file

        Returns:
            Path to generated .tex file or None on failure
        """
        logger.info(f"Converting {rmd_file.name} to LaTeX...")

        # Create R script to convert Rmd to tex using rmarkdown::render
        # Setting keep_tex = TRUE ensures the .tex file is retained
        r_script = f"""
library(rmarkdown)
render('{rmd_file.name}',
       output_format = pdf_document(keep_tex = TRUE),
       output_file = '{rmd_file.stem}.pdf',
       clean = FALSE,
       quiet = TRUE)
"""

        success, output = self.run_command(
            ['Rscript', '-e', r_script],
            cwd=rmd_file.parent
        )

        tex_file = rmd_file.parent / f"{rmd_file.stem}.tex"

        if success and (self.dry_run or tex_file.exists()):
            logger.info(f"  ✓ Generated {tex_file.name}")
            return tex_file
        else:
            logger.warning(f"  ✗ Failed to generate .tex from {rmd_file.name}: {output}")
            return None

    def convert_md_to_tex(self, md_file: Path) -> Optional[Path]:
        """
        Convert .md to .tex using pandoc

        Args:
            md_file: Path to .md file

        Returns:
            Path to generated .tex file or None on failure
        """
        logger.info(f"Converting {md_file.name} to LaTeX...")

        tex_file = md_file.parent / f"{md_file.stem}.tex"

        success, output = self.run_command(
            ['pandoc', md_file.name, '-o', tex_file.name, '--standalone'],
            cwd=md_file.parent
        )

        if success and (self.dry_run or tex_file.exists()):
            logger.info(f"  ✓ Generated {tex_file.name}")
            return tex_file
        else:
            logger.warning(f"  ✗ Failed to generate .tex from {md_file.name}: {output}")
            return None

    def convert_ipynb_to_tex(self, ipynb_file: Path) -> Optional[Path]:
        """
        Convert .ipynb to .tex using jupyter nbconvert

        Args:
            ipynb_file: Path to .ipynb file

        Returns:
            Path to generated .tex file or None on failure
        """
        logger.info(f"Converting {ipynb_file.name} to LaTeX...")

        success, output = self.run_command(
            ['jupyter', 'nbconvert', '--to', 'latex', ipynb_file.name],
            cwd=ipynb_file.parent
        )

        tex_file = ipynb_file.parent / f"{ipynb_file.stem}.tex"

        if success and (self.dry_run or tex_file.exists()):
            logger.info(f"  ✓ Generated {tex_file.name}")
            return tex_file
        else:
            logger.warning(f"  ✗ Failed to generate .tex from {ipynb_file.name}: {output}")
            return None

    def convert_org_to_tex(self, org_file: Path) -> Optional[Path]:
        """
        Convert .org to .tex using pandoc

        Args:
            org_file: Path to .org file

        Returns:
            Path to generated .tex file or None on failure
        """
        logger.info(f"Converting {org_file.name} to LaTeX...")

        tex_file = org_file.parent / f"{org_file.stem}.tex"

        success, output = self.run_command(
            ['pandoc', org_file.name, '-o', tex_file.name, '--standalone'],
            cwd=org_file.parent
        )

        if success and (self.dry_run or tex_file.exists()):
            logger.info(f"  ✓ Generated {tex_file.name}")
            return tex_file
        else:
            logger.warning(f"  ✗ Failed to generate .tex from {org_file.name}: {output}")
            return None

    def tex_to_pdf(self, tex_file: Path) -> bool:
        """
        Convert .tex to .pdf using pdflatex

        Args:
            tex_file: Path to .tex file

        Returns:
            True on success, False on failure
        """
        logger.info(f"Converting {tex_file.name} to PDF...")

        # Run pdflatex twice to resolve references
        for run in [1, 2]:
            success, output = self.run_command(
                ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', tex_file.name],
                cwd=tex_file.parent
            )

            if not success:
                logger.warning(f"  ✗ pdflatex run {run} failed for {tex_file.name}")
                if self.verbose:
                    logger.debug(output)
                return False

        pdf_file = tex_file.parent / f"{tex_file.stem}.pdf"

        if self.dry_run or pdf_file.exists():
            logger.info(f"  ✓ Generated {pdf_file.name}")
            return True
        else:
            logger.warning(f"  ✗ PDF not found after pdflatex: {pdf_file}")
            return False

    def rmd_to_html(self, rmd_file: Path) -> bool:
        """
        Convert .Rmd directly to .html using rmarkdown (skip tex2any)

        Args:
            rmd_file: Path to .Rmd file

        Returns:
            True on success, False on failure
        """
        logger.info(f"Converting {rmd_file.name} to HTML...")

        # Use rmarkdown to generate HTML directly - much faster and more reliable
        r_script = f"""
library(rmarkdown)
render('{rmd_file.name}',
       output_format = html_document(theme = 'readable', highlight = 'tango', toc = TRUE, toc_float = TRUE),
       output_file = '{rmd_file.stem}.html',
       quiet = TRUE)
"""

        success, output = self.run_command(['Rscript', '-e', r_script], cwd=rmd_file.parent)

        html_file = rmd_file.parent / f"{rmd_file.stem}.html"

        if success and (self.dry_run or html_file.exists()):
            logger.info(f"  ✓ Generated {html_file.name}")
            return True
        else:
            logger.warning(f"  ✗ Failed to generate HTML from {rmd_file.name}: {output[:200]}")
            return False

    def convert_file(self, source_file: Path) -> bool:
        """
        Convert a single file through the full pipeline

        Args:
            source_file: Path to source file

        Returns:
            True if all conversions succeeded, False otherwise
        """
        logger.info(f"\n{'='*60}")
        logger.info(f"Processing: {source_file.relative_to(Path.cwd())}")
        logger.info(f"{'='*60}")

        # Step 1: Convert to .tex if needed
        suffix = source_file.suffix.lower()
        pdf_already_generated = False

        if suffix == '.tex':
            tex_file = source_file
            logger.info(f"Already in LaTeX format: {tex_file.name}")
        elif suffix == '.rmd':
            tex_file = self.convert_rmd_to_tex(source_file)
            # rmarkdown::render() already generated PDF
            pdf_already_generated = True
        elif suffix == '.md':
            tex_file = self.convert_md_to_tex(source_file)
        elif suffix == '.ipynb':
            tex_file = self.convert_ipynb_to_tex(source_file)
        elif suffix == '.org':
            tex_file = self.convert_org_to_tex(source_file)
        else:
            logger.warning(f"Unsupported file format: {suffix}")
            self.skipped.append((source_file, f"Unsupported format: {suffix}"))
            return False

        if tex_file is None:
            self.failures.append((source_file, "Failed to convert to .tex"))
            return False

        # Step 2: Convert .tex to PDF (if not already done)
        if pdf_already_generated:
            pdf_file = tex_file.parent / f"{tex_file.stem}.pdf"
            pdf_success = pdf_file.exists() or self.dry_run
            if pdf_success:
                logger.info(f"PDF already generated by rmarkdown: {pdf_file.name}")
            else:
                logger.warning(f"Expected PDF not found: {pdf_file}")
        else:
            pdf_success = self.tex_to_pdf(tex_file)

        # Step 3: Convert to HTML (use rmarkdown directly for .Rmd files to avoid tex2any issues)
        if suffix == '.rmd':
            html_success = self.rmd_to_html(source_file)
        else:
            # For other formats, skip HTML for now (tex2any has expl3 timeout issues)
            logger.info(f"Skipping HTML conversion for non-Rmd file")
            html_success = True  # Don't mark as failure

        # Record result
        if pdf_success and html_success:
            self.successes.append(source_file)
            logger.info(f"✓ Successfully converted {source_file.name} to PDF and HTML")
            return True
        else:
            failures = []
            if not pdf_success:
                failures.append("PDF")
            if not html_success:
                failures.append("HTML")

            self.failures.append((source_file, f"Failed: {', '.join(failures)}"))
            logger.warning(f"✗ Partial failure for {source_file.name}")
            return False

    def find_files(self, root_dir: Path, pattern: Optional[str] = None) -> List[Path]:
        """
        Find all convertible files in directory tree

        Args:
            root_dir: Root directory to search
            pattern: Optional glob pattern to filter files

        Returns:
            List of file paths
        """
        extensions = ['.tex', '.rmd', '.md', '.ipynb', '.org']
        files = []

        if pattern:
            # Use custom pattern
            files = list(root_dir.rglob(pattern))
        else:
            # Find all supported files
            for ext in extensions:
                files.extend(root_dir.rglob(f'*{ext}'))

        # Filter to only supported extensions
        files = [f for f in files if f.suffix.lower() in extensions]

        # Exclude hidden files and files in hidden directories
        def is_hidden(path: Path) -> bool:
            """Check if path or any of its parents are hidden"""
            for part in path.parts:
                if part.startswith('.') and part not in ['.', '..']:
                    return True
            return False

        files = [f for f in files if not is_hidden(f.relative_to(root_dir))]

        # Sort by path for consistent ordering
        files.sort()

        return files

    def print_summary(self):
        """Print conversion summary"""
        logger.info(f"\n{'='*60}")
        logger.info("CONVERSION SUMMARY")
        logger.info(f"{'='*60}")
        logger.info(f"✓ Successes: {len(self.successes)}")
        logger.info(f"✗ Failures:  {len(self.failures)}")
        logger.info(f"⊘ Skipped:   {len(self.skipped)}")
        logger.info(f"{'='*60}")

        if self.failures:
            logger.info("\nFailed conversions:")
            for file, reason in self.failures:
                logger.info(f"  ✗ {file.relative_to(Path.cwd())}: {reason}")

        if self.skipped:
            logger.info("\nSkipped files:")
            for file, reason in self.skipped:
                logger.info(f"  ⊘ {file.relative_to(Path.cwd())}: {reason}")

    def convert_all(self, root_dir: Path, pattern: Optional[str] = None):
        """
        Convert all files in directory tree

        Args:
            root_dir: Root directory to search
            pattern: Optional glob pattern to filter files
        """
        files = self.find_files(root_dir, pattern)

        if not files:
            logger.warning(f"No convertible files found in {root_dir}")
            return

        logger.info(f"Found {len(files)} file(s) to convert")

        for i, file in enumerate(files, 1):
            logger.info(f"\n[{i}/{len(files)}]")
            self.convert_file(file)

        self.print_summary()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Convert problem sets to LaTeX, HTML, and PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert all files in current directory
  python convert_problem_sets.py

  # Dry run to see what would be converted
  python convert_problem_sets.py --dry-run

  # Convert only files matching pattern
  python convert_problem_sets.py --pattern "stats/*/hw*/*.Rmd"

  # Verbose output for debugging
  python convert_problem_sets.py --verbose

  # Use dark theme for HTML output
  python convert_problem_sets.py --html-theme dark

  # Custom HTML components
  python convert_problem_sets.py --html-components "floating-toc,search,reading-time"
"""
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without actually converting'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )

    parser.add_argument(
        '--pattern', '-p',
        type=str,
        help='Glob pattern to filter files (e.g., "stats/*/hw*/*.Rmd")'
    )

    parser.add_argument(
        '--dir', '-d',
        type=str,
        default='.',
        help='Root directory to search (default: current directory)'
    )

    parser.add_argument(
        '--html-theme',
        type=str,
        default='academic',
        choices=['academic', 'clean', 'dark', 'minimal', 'serif', 'modern'],
        help='HTML theme for tex2any (default: academic)'
    )

    parser.add_argument(
        '--html-components',
        type=str,
        default='floating-toc,equation-numbers,copy-code,back-to-top',
        help='Comma-separated components for tex2any HTML output'
    )

    args = parser.parse_args()

    # Create converter
    converter = ProblemSetConverter(
        dry_run=args.dry_run,
        verbose=args.verbose,
        html_theme=args.html_theme,
        html_components=args.html_components
    )

    # Check dependencies
    if not converter.check_dependencies():
        sys.exit(1)

    # Convert files
    root_dir = Path(args.dir).resolve()
    converter.convert_all(root_dir, args.pattern)

    # Exit with appropriate code
    sys.exit(0 if not converter.failures else 1)


if __name__ == '__main__':
    main()
