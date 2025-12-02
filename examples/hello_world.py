#!/usr/bin/env python3
"""
Hello World - Sacred Smoke Example
A simple script to verify Python is working on Android.
"""

import sys
import platform

def main():
    print("=" * 50)
    print("Hello from Sacred Smoke!")
    print("=" * 50)
    print()
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python implementation: {platform.python_implementation()}")
    print()
    print("✅ Python is working correctly on your Android device!")
    print()

if __name__ == "__main__":
    main()
