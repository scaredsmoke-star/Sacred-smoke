# Sacred Smoke Examples

This directory contains example scripts demonstrating how to use Python on Android with Sacred Smoke.

## Running the Examples

To run any example, use:
```bash
python3 example_name.py
```

Or make it executable and run directly:
```bash
chmod +x example_name.py
./example_name.py
```

## Available Examples

### 1. hello_world.py
A simple "Hello World" script that verifies Python is working correctly.

**What it demonstrates:**
- Basic Python execution
- System information access
- Platform detection

**Run it:**
```bash
python3 hello_world.py
```

---

### 2. system_info.py
Displays detailed information about your Python installation and Android device.

**What it demonstrates:**
- Python version and build info
- Platform and architecture details
- OpenSSL configuration
- Environment variables
- Python path configuration

**Run it:**
```bash
python3 system_info.py
```

---

### 3. file_operations.py
Demonstrates basic file input/output operations.

**What it demonstrates:**
- Creating and reading text files
- Working with JSON files
- Directory listing
- File cleanup operations

**Run it:**
```bash
python3 file_operations.py
```

**Note:** This script creates test files and will ask if you want to keep them afterward.

---

### 4. http_server.py
Starts a simple HTTP server that you can access from a browser.

**What it demonstrates:**
- Running a web server on Android
- HTTP request handling
- Serving HTML content
- JSON API endpoints

**Run it:**
```bash
python3 http_server.py
```

**Access the server:**
- Main page: http://localhost:8080
- API endpoint: http://localhost:8080/api

**Note:** Press Ctrl+C to stop the server.

---

## Creating Your Own Scripts

Use these examples as templates for your own Python scripts on Android. Here are some tips:

### Template for a New Script

```python
#!/usr/bin/env python3
"""
Script description here.
"""

import sys

def main():
    print("Your code here")

if __name__ == "__main__":
    main()
```

### Best Practices

1. **Shebang Line**: Start with `#!/usr/bin/env python3` to make scripts executable
2. **Docstrings**: Add documentation at the top of your script
3. **Error Handling**: Use try/except blocks for robust error handling
4. **Resource Management**: Use context managers (`with` statements) for files
5. **User Feedback**: Print clear messages about what your script is doing

### Example with Error Handling

```python
#!/usr/bin/env python3
"""Example with proper error handling."""

import sys

def main():
    try:
        # Your code here
        print("Operation successful!")
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## More Examples Ideas

Here are some ideas for scripts you could create:

### Utility Scripts
- File backup and sync tools
- Text processing and filtering
- Batch file renaming
- Log file analyzer

### Network Scripts
- API clients for web services
- Download managers
- Network diagnostics tools
- Chat applications

### Data Processing
- CSV/Excel data processor
- JSON/XML parser
- Data visualization with matplotlib
- Statistical analysis

### Automation
- Task schedulers
- System monitors
- Automated testing scripts
- Backup automation

## Getting Help

- Check the [main documentation](../README.md)
- Review [usage examples](../docs/USAGE.md)
- Read the [FAQ](../docs/FAQ.md)
- Visit [GitHub Issues](https://github.com/scaredsmoke-star/Sacred-smoke/issues)

## Contributing Examples

Have a useful example to share? We'd love to include it! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

*Happy coding with Sacred Smoke! 🔥*
