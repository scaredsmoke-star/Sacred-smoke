# Installation Guide

This guide provides detailed instructions for installing Python from Sacred Smoke on your Android device.

## Prerequisites

### Device Requirements
- Android device with ARM64 (aarch64) architecture
- Android 5.0 (API level 21) or higher
- At least 100MB of free storage space

### Check Your Device Architecture

To verify your device architecture, you can use:
```bash
uname -m
```

You should see `aarch64` or `arm64`.

## Installation Methods

### Method 1: Using Termux (Recommended)

[Termux](https://termux.dev/) is a terminal emulator for Android that provides a Linux environment.

1. Install Termux from [F-Droid](https://f-droid.org/en/packages/com.termux/) (recommended) or GitHub releases
2. Open Termux and update packages:
   ```bash
   pkg update && pkg upgrade
   ```
3. Install wget or curl:
   ```bash
   pkg install wget
   ```
4. Download the Python tarball:
   ```bash
   wget https://github.com/scaredsmoke-star/Sacred-smoke/raw/main/python-3.14.0-aarch64-linux-android.tar.gz
   ```
5. Extract the archive:
   ```bash
   tar -xzf python-3.14.0-aarch64-linux-android.tar.gz
   ```
6. Move Python to a permanent location:
   ```bash
   mkdir -p ~/.local
   mv python ~/.local/
   ```
7. Add to PATH (add this to `~/.bashrc`):
   ```bash
   echo 'export PATH=$HOME/.local/python/bin:$PATH' >> ~/.bashrc
   source ~/.bashrc
   ```
8. Verify installation:
   ```bash
   python3 --version
   ```

### Method 2: Using ADB (Advanced)

If you have ADB access to your device:

1. Download the tarball to your computer
2. Connect your device via ADB
3. Push the file to your device:
   ```bash
   adb push python-3.14.0-aarch64-linux-android.tar.gz /sdcard/
   ```
4. Connect to device shell:
   ```bash
   adb shell
   ```
5. Navigate and extract:
   ```bash
   cd /sdcard/
   tar -xzf python-3.14.0-aarch64-linux-android.tar.gz
   ```
6. Follow similar PATH setup as Method 1

### Method 3: Manual Installation

1. Download the tarball directly on your Android device using a browser
2. Use a file manager app to locate the downloaded file
3. Use a terminal app to extract and set up as described above

## Post-Installation

### Install pip packages

Once Python is installed, you can install packages using pip:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install your-package-name
```

### Test Your Installation

Create a test script:
```python
# test.py
import sys
import ssl
import sqlite3

print(f"Python version: {sys.version}")
print(f"SSL support: {ssl.OPENSSL_VERSION}")
print(f"SQLite version: {sqlite3.sqlite_version}")
print("Python is working correctly on Android!")
```

Run it:
```bash
python3 test.py
```

## Troubleshooting

### Permission Denied Errors
If you get permission errors, make sure the Python binary is executable:
```bash
chmod +x ~/.local/python/bin/python3
```

### Missing Libraries
If you encounter missing library errors, ensure you extracted the complete tarball and all shared libraries are present.

### Path Issues
If Python is not found after installation, verify your PATH:
```bash
echo $PATH
which python3
```

## Uninstallation

To remove Python:
```bash
rm -rf ~/.local/python
```

Remove the PATH export from your `~/.bashrc` file.

## Need Help?

If you encounter issues:
1. Check the [main README](../README.md)
2. Visit the [GitHub Issues](https://github.com/scaredsmoke-star/Sacred-smoke/issues)
3. Consult the [Python documentation](https://docs.python.org/3/using/android.html)
