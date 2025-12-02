#!/usr/bin/env python3
"""
File Operations - Sacred Smoke Example
Demonstrates basic file I/O operations on Android.
"""

import os
import json
from datetime import datetime

def create_sample_file():
    """Create a sample text file."""
    filename = "sacred_smoke_test.txt"
    content = f"""Sacred Smoke - Python for Android
Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This is a test file created by Python running on Android.
File operations are working correctly!
"""
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"✓ Created: {filename}")
    return filename

def read_file(filename):
    """Read and display file contents."""
    print(f"\n--- Contents of {filename} ---")
    with open(filename, 'r') as f:
        content = f.read()
        print(content)
    print("--- End of file ---\n")

def create_json_file():
    """Create a JSON configuration file."""
    filename = "config.json"
    data = {
        "app_name": "Sacred Smoke Demo",
        "version": "1.0.0",
        "platform": "Android",
        "python_version": "3.14.0",
        "created": datetime.now().isoformat(),
        "settings": {
            "debug": True,
            "max_connections": 100,
            "timeout": 30
        }
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Created: {filename}")
    return filename

def read_json_file(filename):
    """Read and display JSON file contents."""
    with open(filename, 'r') as f:
        data = json.load(f)
    
    print(f"\n--- JSON Data from {filename} ---")
    print(json.dumps(data, indent=2))
    print("--- End of JSON ---\n")

def list_files():
    """List files in current directory."""
    print("--- Files in current directory ---")
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for i, filename in enumerate(files, 1):
        size = os.path.getsize(filename)
        print(f"{i}. {filename} ({size} bytes)")
    print(f"\nTotal files: {len(files)}\n")

def cleanup(files):
    """Remove created test files."""
    print("Cleaning up test files...")
    for filename in files:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"✓ Removed: {filename}")

def main():
    print("=" * 60)
    print("Sacred Smoke - File Operations Example")
    print("=" * 60)
    print()
    
    created_files = []
    
    # Create and read text file
    print("1. Creating and reading text file...")
    txt_file = create_sample_file()
    created_files.append(txt_file)
    read_file(txt_file)
    
    # Create and read JSON file
    print("2. Creating and reading JSON file...")
    json_file = create_json_file()
    created_files.append(json_file)
    read_json_file(json_file)
    
    # List all files
    print("3. Listing files in directory...")
    list_files()
    
    # Ask if user wants to keep files
    try:
        keep = input("Keep test files? (y/n): ").lower()
        if keep != 'y':
            cleanup(created_files)
        else:
            print(f"\nTest files kept: {', '.join(created_files)}")
    except (EOFError, KeyboardInterrupt):
        print("\n\nTest files kept.")
    
    print("\n" + "=" * 60)
    print("File operations example complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
