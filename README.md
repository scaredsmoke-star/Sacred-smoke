# Sacred Smoke

Python 3.14.0 for Android (aarch64-linux-android)

## Overview

Sacred Smoke provides pre-compiled Python binaries and libraries for Android devices with ARM64 architecture. This project makes it easier to run Python applications on Android without needing to compile Python from source.

## What's Included

- **Python 3.14.0** - Latest Python interpreter compiled for Android
- **OpenSSL** - Cryptography support with headers and libraries
- **Android Build Scripts** - Tools for building Python modules on Android
- **Test Suite** - Comprehensive tests for Android compatibility

## Package Contents

The distribution tarball (`python-3.14.0-aarch64-linux-android.tar.gz`) contains:
- Pre-compiled Python libraries
- Python standard library modules
- Android-specific patches and configurations
- Development headers for building extensions

## Quick Start

**🚀 Want to get started fast?** See the [Quick Start Guide](QUICKSTART.md) for common commands and snippets.

### Prerequisites
- Android device or emulator with ARM64 (aarch64) architecture
- Android 5.0 (API level 21) or higher
- Terminal emulator app (like Termux) or ADB access

### Installation

1. Download the tarball:
   ```bash
   wget https://github.com/scaredsmoke-star/Sacred-smoke/raw/main/python-3.14.0-aarch64-linux-android.tar.gz
   ```

2. Extract the archive:
   ```bash
   tar -xzf python-3.14.0-aarch64-linux-android.tar.gz
   ```

3. Add Python to your PATH:
   ```bash
   export PATH=$PATH:$(pwd)/python/bin
   ```

4. Verify installation:
   ```bash
   python3 --version
   ```

## Usage

Once installed, you can use Python as you normally would:

```bash
python3 your_script.py
```

Or start an interactive Python shell:

```bash
python3
```

## Building from Source

If you need to rebuild or customize Python for Android, refer to the [official Python documentation](https://docs.python.org/3/using/android.html) for detailed instructions.

## Compatibility

- **Architecture**: aarch64-linux-android (ARM64)
- **Minimum Android Version**: Android 5.0 (API 21)
- **Python Version**: 3.14.0

## Resources

- [Python Documentation](https://docs.python.org/3/)
- [Python on Android Guide](https://docs.python.org/3/using/android.html)
- [GitHub Repository](https://github.com/scaredsmoke-star/Sacred-smoke)

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/scaredsmoke-star/Sacred-smoke) and open an issue.

## License

This project follows Python's licensing. See the Python Software Foundation License for details.

---

*Sacred Smoke - Bringing Python to Android*
