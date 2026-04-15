#!/bin/bash
#
# Check all dependencies for problem set conversion
#

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_header() {
    echo -e "\n${BLUE}=== $1 ===${NC}"
}

print_ok() {
    echo -e "${GREEN}✓${NC} $1"
}

print_fail() {
    echo -e "${RED}✗${NC} $1"
}

print_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

ERRORS=0
WARNINGS=0

print_header "System Tools"

# Check system tools
for tool in pdflatex pandoc Rscript; do
    if command -v "$tool" &> /dev/null; then
        version=$(case "$tool" in
            pdflatex) pdflatex --version | head -1 ;;
            pandoc) pandoc --version | head -1 ;;
            Rscript) Rscript --version 2>&1 | head -1 ;;
        esac)
        print_ok "$tool - $version"
    else
        print_fail "$tool not found"
        ((ERRORS++))
    fi
done

# Check tex2any
print_header "tex2any"
if command -v tex2any &> /dev/null; then
    version=$(tex2any --version 2>&1 | head -1)
    print_ok "tex2any - $version"

    # Check LaTeXML dependency
    if command -v latexml &> /dev/null; then
        latexml_version=$(latexml --version 2>&1 | head -1)
        print_ok "LaTeXML - $latexml_version"
    else
        print_fail "LaTeXML not found (required by tex2any)"
        ((ERRORS++))
    fi
else
    print_fail "tex2any not found"
    ((ERRORS++))
fi

# Check R packages
print_header "R Packages"

# Set R_LIBS to include user library
export R_LIBS="$HOME/R/library:${R_LIBS:-}"

check_r_package() {
    package=$1
    if Rscript -e "library($package)" &> /dev/null; then
        version=$(Rscript -e "cat(as.character(packageVersion('$package')))" 2>/dev/null)
        print_ok "$package (version $version)"
        return 0
    else
        print_fail "$package not installed"
        return 1
    fi
}

for pkg in knitr rmarkdown; do
    if ! check_r_package "$pkg"; then
        ((ERRORS++))
    fi
done

# Check optional R packages
print_header "Optional R Packages"
for pkg in readxl printr; do
    if ! check_r_package "$pkg"; then
        print_warn "$pkg not installed (may be needed for some documents)"
        ((WARNINGS++))
    fi
done

# Check Python
print_header "Python Environment"

if command -v python &> /dev/null; then
    python_version=$(python --version)
    print_ok "$python_version"
else
    print_fail "Python not found"
    ((ERRORS++))
fi

# Summary
print_header "Summary"

if [ $ERRORS -eq 0 ]; then
    print_ok "All required dependencies are installed!"
    if [ $WARNINGS -gt 0 ]; then
        echo -e "\n${YELLOW}Note: $WARNINGS optional package(s) missing.${NC}"
        echo "Some documents may fail if they depend on these packages."
    fi
    echo -e "\n${GREEN}You can start converting files!${NC}"
    echo "Try: ./convert.sh dry-run"
    exit 0
else
    echo -e "\n${RED}$ERRORS required dependencies are missing.${NC}"
    echo -e "\n${YELLOW}Installation instructions:${NC}"
    echo ""
    echo "R packages:"
    echo "  R -e 'install.packages(c(\"knitr\", \"rmarkdown\", \"readxl\", \"printr\"))'"
    echo ""
    echo "LaTeXML (for tex2any):"
    echo "  Ubuntu/Debian: sudo apt-get install latexml"
    echo "  macOS: brew install latexml"
    echo "  Or via cpanm: cpanm LaTeXML"
    echo ""
    echo "Other tools (Ubuntu/Debian):"
    echo "  sudo apt-get install texlive-latex-base texlive-latex-extra pandoc"
    echo ""
    exit 1
fi
