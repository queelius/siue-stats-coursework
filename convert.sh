#!/bin/bash
#
# Simple wrapper script for converting problem sets
# Usage: ./convert.sh [options]
#

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONVERTER="$SCRIPT_DIR/convert_problem_sets.py"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Print colored message
print_msg() {
    echo -e "${2}${1}${NC}"
}

# Check if Python script exists
if [ ! -f "$CONVERTER" ]; then
    print_msg "Error: $CONVERTER not found!" "$RED"
    exit 1
fi

# If no arguments, show help
if [ $# -eq 0 ]; then
    cat << 'EOF'
Problem Set Conversion Tool - Quick Wrapper

Usage:
  ./convert.sh [command] [options]

Commands:
  all               - Convert all files (same as no arguments with --dry-run)
  dry-run          - Show what would be converted without converting
  test FILE        - Test conversion on a single file
  course PATTERN   - Convert all files matching pattern
  help             - Show this help message

Quick Examples:
  ./convert.sh dry-run                                    # Preview what would happen
  ./convert.sh test "stats/stat581_fa2021/hw1/hw1.Rmd"   # Test single file
  ./convert.sh course "stats/stat581_fa2021/**/*.Rmd"    # Convert entire course
  ./convert.sh all                                       # Convert everything (use with caution!)

Advanced:
  Run the Python script directly for full control:
    python convert_problem_sets.py --help

Documentation:
  QUICKSTART.md      - Quick start guide
  CONVERSION_README.md - Full documentation

EOF
    exit 0
fi

# Parse command
case "$1" in
    help|--help|-h)
        exec "$0"
        ;;

    dry-run)
        print_msg "Running dry-run on all files..." "$YELLOW"
        python "$CONVERTER" --dry-run "${@:2}"
        ;;

    test)
        if [ -z "$2" ]; then
            print_msg "Error: Please specify a file to test" "$RED"
            echo "Usage: ./convert.sh test FILE"
            exit 1
        fi
        print_msg "Testing conversion on: $2" "$YELLOW"
        python "$CONVERTER" --verbose --pattern "$2" "${@:3}"
        ;;

    course)
        if [ -z "$2" ]; then
            print_msg "Error: Please specify a pattern" "$RED"
            echo "Usage: ./convert.sh course PATTERN"
            echo "Example: ./convert.sh course 'stats/stat581_fa2021/**/*.Rmd'"
            exit 1
        fi
        print_msg "Converting files matching: $2" "$YELLOW"
        python "$CONVERTER" --pattern "$2" "${@:3}"
        ;;

    all)
        print_msg "WARNING: This will convert ALL files in the repository!" "$RED"
        read -p "Are you sure? (yes/no): " confirm
        if [ "$confirm" = "yes" ]; then
            print_msg "Converting all files..." "$YELLOW"
            python "$CONVERTER" "${@:2}"
        else
            print_msg "Cancelled." "$YELLOW"
            exit 0
        fi
        ;;

    *)
        # Pass through to Python script
        python "$CONVERTER" "$@"
        ;;
esac
