# Sacred Smoke - Quick Reference

A quick guide for common tasks with Sacred Smoke.

## Installation

### One-Line Install (Recommended)
```bash
wget https://github.com/scaredsmoke-star/Sacred-smoke/raw/main/install.sh && bash install.sh
```

### Manual Install
```bash
# Download
wget https://github.com/scaredsmoke-star/Sacred-smoke/raw/main/python-3.14.0-aarch64-linux-android.tar.gz

# Extract
tar -xzf python-3.14.0-aarch64-linux-android.tar.gz

# Add to PATH
export PATH=$PATH:$(pwd)/python/bin

# Make permanent (add to ~/.bashrc)
echo 'export PATH=$HOME/.local/python/bin:$PATH' >> ~/.bashrc
```

## Common Commands

### Check Python Version
```bash
python3 --version
```

### Run Python Script
```bash
python3 script.py
```

### Interactive Python Shell
```bash
python3
```

### Install Package
```bash
python3 -m pip install package-name
```

### Upgrade pip
```bash
python3 -m pip install --upgrade pip
```

### List Installed Packages
```bash
python3 -m pip list
```

### Create Virtual Environment
```bash
python3 -m venv myenv
source myenv/bin/activate
```

## Quick Tests

### Test Python
```bash
python3 -c "print('Hello from Sacred Smoke!')"
```

### Test SSL
```bash
python3 -c "import ssl; print(ssl.OPENSSL_VERSION)"
```

### Test JSON
```bash
python3 -c "import json; print(json.dumps({'status': 'ok'}))"
```

### System Info
```bash
python3 -c "import platform; print(f'{platform.system()} {platform.machine()}')"
```

## Troubleshooting Quick Fixes

### Python Not Found
```bash
# Check PATH
echo $PATH

# Add to current session
export PATH=$HOME/.local/python/bin:$PATH

# Make permanent
echo 'export PATH=$HOME/.local/python/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Permission Denied
```bash
chmod +x ~/.local/python/bin/python3
```

### Import Errors
```bash
# Check Python path
python3 -c "import sys; print('\n'.join(sys.path))"

# Reinstall if needed
rm -rf ~/.local/python
# Run install script again
```

### SSL Certificate Errors
```bash
python3 -m pip install --upgrade certifi
```

## Useful Snippets

### File Operations
```python
# Write file
with open('file.txt', 'w') as f:
    f.write('Hello, Sacred Smoke!')

# Read file
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
```

### HTTP Request
```python
import urllib.request
response = urllib.request.urlopen('https://api.github.com')
print(response.read().decode())
```

### JSON Operations
```python
import json

# Write JSON
data = {'name': 'Sacred Smoke', 'version': '1.0'}
with open('data.json', 'w') as f:
    json.dump(data, f)

# Read JSON
with open('data.json', 'r') as f:
    data = json.load(f)
```

### Simple Web Server
```python
python3 -m http.server 8000
# Access at http://localhost:8000
```

## Popular Packages

### Web Development
```bash
pip install flask         # Micro web framework
pip install requests      # HTTP library
pip install beautifulsoup4  # HTML parser
```

### Data Science
```bash
pip install pandas        # Data analysis
pip install numpy         # Numerical computing
pip install matplotlib    # Plotting
```

### Utilities
```bash
pip install pillow        # Image processing
pip install pyyaml        # YAML parser
pip install python-dotenv # Environment variables
```

## Resources

- **Full Documentation**: [README.md](README.md)
- **Installation Guide**: [docs/INSTALLATION.md](docs/INSTALLATION.md)
- **Usage Examples**: [docs/USAGE.md](docs/USAGE.md)
- **FAQ**: [docs/FAQ.md](docs/FAQ.md)
- **GitHub**: https://github.com/scaredsmoke-star/Sacred-smoke

## Need Help?

1. Check the [FAQ](docs/FAQ.md)
2. Review the [examples](examples/)
3. Open an issue on GitHub
4. Read the Python documentation

---

*Sacred Smoke - Python on Android made simple* 🔥
