#!/usr/bin/env python3
"""
Problem Set Converter - LaTeX and PDF only (skips HTML)
Fast conversion without tex2any delays
"""

import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple, Optional

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class QuickConverter:
    def __init__(self, dry_run: bool = False, verbose: bool = False):
        self.dry_run = dry_run
        self.verbose = verbose
        self.successes = []
        self.failures = []

        if verbose:
            logger.setLevel(logging.DEBUG)

    def run_command(self, cmd: List[str], cwd: Optional[Path] = None) -> Tuple[bool, str]:
        if self.dry_run:
            logger.info(f"[DRY RUN] Would execute: {' '.join(cmd)}")
            return True, ""

        try:
            env = os.environ.copy()
            home = os.path.expanduser("~")
            r_libs_user = os.path.join(home, "R", "library")
            if os.path.exists(r_libs_user):
                existing_libs = env.get('R_LIBS', '')
                env['R_LIBS'] = f"{r_libs_user}:{existing_libs}" if existing_libs else r_libs_user

            result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=300, env=env)

            if result.returncode != 0:
                return False, result.stderr or result.stdout
            return True, result.stdout

        except subprocess.TimeoutExpired:
            return False, "Command timed out"
        except Exception as e:
            return False, str(e)

    def convert_rmd(self, rmd_file: Path) -> bool:
        logger.info(f"Converting {rmd_file.relative_to(Path.cwd())}...")

        r_script = f"""
library(rmarkdown)
render('{rmd_file.name}',
       output_format = pdf_document(keep_tex = TRUE),
       output_file = '{rmd_file.stem}.pdf',
       clean = FALSE,
       quiet = TRUE)
"""

        success, output = self.run_command(['Rscript', '-e', r_script], cwd=rmd_file.parent)

        tex_file = rmd_file.parent / f"{rmd_file.stem}.tex"
        pdf_file = rmd_file.parent / f"{rmd_file.stem}.pdf"

        if success and (self.dry_run or (tex_file.exists() and pdf_file.exists())):
            logger.info(f"  ✓ {rmd_file.name} → {rmd_file.stem}.tex + {rmd_file.stem}.pdf")
            self.successes.append(rmd_file)
            return True
        else:
            error_msg = output.split('\n')[0] if output else "Unknown error"
            logger.warning(f"  ✗ {rmd_file.name}: {error_msg[:100]}")
            self.failures.append((rmd_file, error_msg[:200]))
            return False

    def find_files(self, root_dir: Path, pattern: Optional[str] = None) -> List[Path]:
        if pattern:
            files = list(root_dir.rglob(pattern))
        else:
            files = list(root_dir.rglob('*.Rmd'))

        # Exclude hidden files and directories
        def is_hidden(path: Path) -> bool:
            for part in path.parts:
                if part.startswith('.') and part not in ['.', '..']:
                    return True
            return False

        files = [f for f in files if not is_hidden(f.relative_to(root_dir))]
        files.sort()
        return files

    def convert_all(self, root_dir: Path, pattern: Optional[str] = None):
        files = self.find_files(root_dir, pattern)

        if not files:
            logger.warning(f"No files found")
            return

        logger.info(f"Found {len(files)} file(s) to convert\n")

        for i, file in enumerate(files, 1):
            logger.info(f"[{i}/{len(files)}]")
            self.convert_rmd(file)

        logger.info(f"\n{'='*60}")
        logger.info("CONVERSION SUMMARY")
        logger.info(f"{'='*60}")
        logger.info(f"✓ Successes: {len(self.successes)}")
        logger.info(f"✗ Failures:  {len(self.failures)}")
        logger.info(f"{'='*60}")

        if self.failures:
            logger.info("\nFailed conversions (first 20):")
            for file, reason in self.failures[:20]:
                logger.info(f"  ✗ {file.relative_to(Path.cwd())}")
                if self.verbose:
                    logger.info(f"     Reason: {reason}")

def main():
    parser = argparse.ArgumentParser(description="Fast LaTeX/PDF conversion (no HTML)")
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--verbose', '-v', action='store_true')
    parser.add_argument('--pattern', '-p', type=str)
    parser.add_argument('--dir', '-d', type=str, default='.')

    args = parser.parse_args()

    converter = QuickConverter(dry_run=args.dry_run, verbose=args.verbose)
    root_dir = Path(args.dir).resolve()
    converter.convert_all(root_dir, args.pattern)

    sys.exit(0 if not converter.failures else 1)

if __name__ == '__main__':
    main()
