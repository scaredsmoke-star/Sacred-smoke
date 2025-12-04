#!/bin/bash

# Sacred Smoke - Local Development Server Launch Script
# This script launches a local web server to preview and develop the Sacred Smoke website

set -e

echo "=================================="
echo "Sacred Smoke - Launch Website"
echo "=================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}Python 3 not found. Trying python...${NC}"
    if ! command -v python &> /dev/null; then
        echo "Error: Python is not installed. Please install Python to run the local server."
        exit 1
    fi
    PYTHON_CMD="python"
else
    PYTHON_CMD="python3"
fi

echo -e "${GREEN}✓ Python found: $PYTHON_CMD${NC}"
echo ""

# Default port
PORT="${1:-8000}"

echo "Starting web server..."
echo -e "${CYAN}Server will be available at:${NC}"
echo -e "  ${GREEN}http://localhost:$PORT${NC}"
echo -e "  ${GREEN}http://127.0.0.1:$PORT${NC}"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "=================================="
echo ""

# Change to script directory and start server
cd "$SCRIPT_DIR"
$PYTHON_CMD -m http.server $PORT
