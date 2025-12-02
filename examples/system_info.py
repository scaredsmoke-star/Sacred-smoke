#!/usr/bin/env python3
"""
System Information - Sacred Smoke Example
Displays detailed information about your Python installation and device.
"""

import sys
import platform
import os
import ssl

def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def main():
    print_section("Python Information")
    print(f"Version: {sys.version}")
    print(f"Implementation: {platform.python_implementation()}")
    print(f"Compiler: {platform.python_compiler()}")
    print(f"Build: {platform.python_build()}")
    print(f"Executable: {sys.executable}")
    
    print_section("Platform Information")
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {platform.architecture()}")
    
    print_section("OpenSSL Information")
    print(f"OpenSSL Version: {ssl.OPENSSL_VERSION}")
    print(f"OpenSSL Version Info: {ssl.OPENSSL_VERSION_INFO}")
    
    print_section("Environment")
    print(f"Current Directory: {os.getcwd()}")
    print(f"HOME: {os.environ.get('HOME', 'Not set')}")
    print(f"USER: {os.environ.get('USER', 'Not set')}")
    print(f"SHELL: {os.environ.get('SHELL', 'Not set')}")
    
    print_section("Python Path")
    for i, path in enumerate(sys.path, 1):
        print(f"{i}. {path}")
    
    print("\n" + "=" * 60)
    print("  System check complete!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
