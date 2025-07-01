#!/bin/bash

# ===================================================================
#  🤖 Elderly Care QA Dataset Manager - Unix Launcher
#  Advanced tool for generating conversational datasets
# ===================================================================

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Banner
echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                 🤖 ELDERLY CARE QA MANAGER                   ║"
echo "║                                                              ║"
echo "║     Advanced Dataset Generator for Elderly Care Chatbots    ║"
echo "║                    Powered by Google Gemini                 ║"
echo "║                                                              ║"
echo "║                       Unix Launcher                         ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Function to show help
show_help() {
    echo -e "\n${YELLOW}🎯 USAGE:${NC}"
    echo "  ./run.sh                    # Interactive menu mode"
    echo "  ./run.sh --check           # Check Google API connection"
    echo "  ./run.sh --demo            # Generate demo dataset"
    echo "  ./run.sh --marathon        # Start marathon generation"
    echo "  ./run.sh --merge           # Merge CSV files"
    echo "  ./run.sh --analyze         # Analyze datasets"
    echo "  ./run.sh --clean           # Clean output directories"
    echo "  ./run.sh --info            # Show system information"
    echo "  ./run.sh --help            # Show this help"
    echo ""
    exit 0
}

# Function to check Python
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Python 3 is not installed or not in PATH${NC}"
        echo "Please install Python 3.7+ from your package manager"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Python 3 found: $(python3 --version)${NC}"
}

# Function to setup virtual environment
setup_venv() {
    if [ ! -d ".venv" ]; then
        echo -e "${YELLOW}🔄 Creating virtual environment...${NC}"
        python3 -m venv .venv
        if [ $? -ne 0 ]; then
            echo -e "${RED}❌ Failed to create virtual environment${NC}"
            exit 1
        fi
    fi
    
    echo -e "${YELLOW}🔌 Activating virtual environment...${NC}"
    source .venv/bin/activate
    
    if [ $? -ne 0 ]; then
        echo -e "${RED}❌ Failed to activate virtual environment${NC}"
        exit 1
    fi
}

# Function to check and install dependencies
check_dependencies() {
    echo -e "${YELLOW}🔍 Checking dependencies...${NC}"
    
    if ! python -c "import google.generativeai, pandas, dotenv" &> /dev/null; then
        echo -e "${YELLOW}📦 Installing dependencies...${NC}"
        pip install -r requirements.txt
        
        if [ $? -ne 0 ]; then
            echo -e "${RED}❌ Failed to install dependencies${NC}"
            exit 1
        fi
    else
        echo -e "${GREEN}✅ All dependencies are installed${NC}"
    fi
}

# Function to run the manager
run_manager() {
    local command="$1"
    
    if [ -z "$command" ]; then
        echo -e "${GREEN}✅ Starting interactive mode...${NC}"
        python qa_manager.py
    else
        echo -e "${GREEN}✅ Running command: $command${NC}"
        python qa_manager.py "$command"
    fi
}

# Main execution
main() {
    # Parse arguments
    case "$1" in
        --help|-h)
            show_help
            ;;
        --check|--demo|--marathon|--merge|--analyze|--clean|--info)
            COMMAND="$1"
            ;;
        "")
            COMMAND=""
            ;;
        *)
            echo -e "${RED}❌ Unknown argument: $1${NC}"
            show_help
            ;;
    esac
    
    # Setup environment
    check_python
    setup_venv
    check_dependencies
    
    # Run the manager
    run_manager "$COMMAND"
    
    echo -e "\n${CYAN}👋 Thank you for using QA Dataset Manager!${NC}"
}

# Make script executable if not already
if [ ! -x "$0" ]; then
    chmod +x "$0"
fi

# Run main function
main "$@"
