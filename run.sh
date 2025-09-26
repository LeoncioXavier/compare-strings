#!/bin/bash

# compare-strings setup and run script
# This script creates a Python virtual environment, installs dependencies,
# and runs the compare-strings tool

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if Python is installed
check_python() {
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3.8 or higher."
        exit 1
    fi

    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    print_info "Found Python $PYTHON_VERSION"

    # Check if version is >= 3.8
    if python3 -c 'import sys; exit(0 if sys.version_info >= (3, 8) else 1)'; then
        print_success "Python version is compatible (>= 3.8)"
    else
        print_error "Python 3.8 or higher is required. Current version: $PYTHON_VERSION"
        exit 1
    fi
}

# Create virtual environment
create_venv() {
    if [ -d "venv" ]; then
        print_warning "Virtual environment already exists. Removing and recreating..."
        rm -rf venv
    fi

    print_info "Creating Python virtual environment..."
    python3 -m venv venv
    print_success "Virtual environment created"
}

# Activate virtual environment and install dependencies
setup_dependencies() {
    print_info "Activating virtual environment and installing dependencies..."

    # Activate virtual environment
    source venv/bin/activate

    # Upgrade pip
    pip install --upgrade pip

    # Install the package in development mode
    pip install -e .

    # Install development dependencies
    pip install -e ".[dev]"

    print_success "Dependencies installed successfully"
}

# Run the compare-strings script
run_script() {
    print_info "Running compare-strings script..."

    if [ $# -eq 0 ]; then
        print_warning "No arguments provided. Running with default test strings..."
        compare-strings "hello" "hello"
        echo ""
        compare-strings "ab" "abc"
    else
        compare-strings "$@"
    fi
}

# Main execution
main() {
    echo -e "${BLUE}🚀 compare-strings Setup and Run Script${NC}"
    echo "========================================"

    # Check Python installation
    check_python

    # Create virtual environment
    create_venv

    # Setup dependencies
    setup_dependencies

    # Run the script with provided arguments
    echo ""
    echo -e "${BLUE}🎯 Running compare-strings${NC}"
    echo "=============================="

    # Pass all arguments to the run_script function
    run_script "$@"

    echo ""
    print_success "Script execution completed!"
    print_info "To run again later, activate the virtual environment:"
    echo "  source venv/bin/activate"
    echo "  compare-strings \"string1\" \"string2\""
}

# Run main function with all script arguments
main "$@"