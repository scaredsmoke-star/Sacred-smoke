#!/bin/bash

# Sacred Smoke - Python 3.14.0 for Android Installation Script
# This script helps automate the installation process

set -e

echo "=================================="
echo "Sacred Smoke - Python for Android"
echo "=================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check architecture
ARCH=$(uname -m)
echo "Detected architecture: $ARCH"

if [ "$ARCH" != "aarch64" ] && [ "$ARCH" != "arm64" ]; then
    echo -e "${RED}Error: This package is for aarch64/arm64 architecture only.${NC}"
    echo "Your architecture: $ARCH"
    exit 1
fi

echo -e "${GREEN}✓ Architecture compatible${NC}"
echo ""

# Set installation directory
INSTALL_DIR="${HOME}/.local/python3.14"
echo "Installation directory: $INSTALL_DIR"

# Check if already installed
if [ -d "$INSTALL_DIR" ]; then
    echo -e "${YELLOW}Warning: Python installation already exists at $INSTALL_DIR${NC}"
    read -p "Do you want to overwrite it? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 0
    fi
    rm -rf "$INSTALL_DIR"
fi

# Check for tarball
TARBALL="python-3.14.0-aarch64-linux-android.tar.gz"

if [ ! -f "$TARBALL" ]; then
    echo -e "${YELLOW}Tarball not found. Downloading...${NC}"
    
    # Try to download
    if command -v wget &> /dev/null; then
        wget "https://github.com/scaredsmoke-star/Sacred-smoke/raw/main/$TARBALL"
    elif command -v curl &> /dev/null; then
        curl -LO "https://github.com/scaredsmoke-star/Sacred-smoke/raw/main/$TARBALL"
    else
        echo -e "${RED}Error: Neither wget nor curl found. Please install one of them.${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}✓ Tarball found${NC}"
echo ""

# Extract
echo "Extracting Python..."
mkdir -p "$INSTALL_DIR"
tar -xzf "$TARBALL" -C "$INSTALL_DIR" --strip-components=1

echo -e "${GREEN}✓ Extraction complete${NC}"
echo ""

# Make binaries executable
chmod +x "$INSTALL_DIR/bin/"*

# Add to PATH
SHELL_RC=""
if [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
else
    SHELL_RC="$HOME/.profile"
fi

echo "Updating PATH in $SHELL_RC..."

# Check if already in PATH
if ! grep -q "python3.14/bin" "$SHELL_RC" 2>/dev/null; then
    echo "" >> "$SHELL_RC"
    echo "# Sacred Smoke - Python 3.14.0" >> "$SHELL_RC"
    echo "export PATH=\"\$HOME/.local/python3.14/bin:\$PATH\"" >> "$SHELL_RC"
    echo -e "${GREEN}✓ PATH updated${NC}"
else
    echo -e "${YELLOW}PATH already contains Python directory${NC}"
fi

echo ""
echo "=================================="
echo -e "${GREEN}Installation Complete!${NC}"
echo "=================================="
echo ""
echo "To start using Python, run:"
echo "  source $SHELL_RC"
echo ""
echo "Or restart your terminal session."
echo ""
echo "Verify installation with:"
echo "  python3 --version"
echo ""
echo "Quick test:"
echo "  python3 -c 'print(\"Hello from Python on Android!\")'"
echo ""
echo "To install packages:"
echo "  python3 -m pip install package-name"
echo ""
echo "For more information, visit:"
echo "  https://github.com/scaredsmoke-star/Sacred-smoke"
echo ""
