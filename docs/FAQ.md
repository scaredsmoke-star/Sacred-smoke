# Frequently Asked Questions (FAQ)

## General Questions

### What is Sacred Smoke?

Sacred Smoke is a distribution of Python 3.14.0 pre-compiled for Android devices with ARM64 (aarch64) architecture. It allows you to run Python scripts and applications on your Android device without needing to compile Python from source.

### Why would I use Sacred Smoke instead of compiling Python myself?

Compiling Python for Android can be complex and time-consuming. Sacred Smoke provides:
- Pre-compiled binaries ready to use
- Proper configuration for Android
- OpenSSL and other essential libraries included
- Tested and verified on Android devices

### Is Sacred Smoke free?

Yes! Sacred Smoke is released under the MIT License, making it free and open source.

## Compatibility

### What devices are supported?

Sacred Smoke supports:
- **Architecture**: ARM64/aarch64 (64-bit ARM processors)
- **Android Version**: Android 5.0 (API level 21) or higher
- Most modern Android devices since 2014

### How do I check if my device is compatible?

Run this command in Termux or a terminal app:
```bash
uname -m
```

If the output is `aarch64` or `arm64`, your device is compatible.

### Will this work on 32-bit ARM devices?

No, this package is specifically for 64-bit ARM (aarch64) devices. 32-bit ARM devices require a different build.

### Can I use this on Android emulators?

Yes, as long as the emulator is configured with ARM64 architecture and runs Android 5.0 or higher.

## Installation

### Where should I install Python?

Recommended locations:
- **Termux**: `~/.local/python` or `$PREFIX/python`
- **Regular Android**: `/data/local/tmp/python` (requires root for some locations)
- **SD Card**: `/sdcard/python` (may have permission restrictions)

### Do I need root access?

No, root access is not required. You can install and use Python in user-accessible directories.

### How much storage space do I need?

You'll need approximately:
- ~20MB for the compressed tarball
- ~100MB for the extracted Python installation
- Additional space for packages you install via pip

### The download is very slow, what can I do?

You can:
- Try a different network connection
- Download on a computer and transfer via ADB
- Use a download manager app
- Check if GitHub is accessible in your region

## Usage

### Can I install pip packages?

Yes! Use pip to install packages:
```bash
python3 -m pip install package-name
```

Note: Some packages with C extensions may require compilation and additional build tools.

### Which packages work on Android?

Most pure Python packages work without issues. Packages with C extensions may need:
- Compatible binaries for Android
- Build tools to compile from source
- Some may not work due to Android limitations

Popular packages that work well:
- requests, urllib3
- Flask, FastAPI
- pandas, numpy (may require special builds)
- SQLAlchemy
- BeautifulSoup4, lxml
- Pillow (with proper build)

### Can I run Django or Flask web applications?

Yes! Both Django and Flask work on Android. However:
- Use development servers, not production servers
- Be mindful of battery consumption
- Network access may require proper firewall configuration

### How do I run Python scripts automatically?

You can:
- Use Termux's `termux-job-scheduler` for scheduled tasks
- Create shell scripts that launch Python
- Use Android automation apps like Tasker with Termux integration

## Troubleshooting

### Python command not found

Solutions:
1. Ensure Python is extracted properly
2. Check your PATH: `echo $PATH`
3. Add Python to PATH: `export PATH=$PATH:/path/to/python/bin`
4. Add the export to `~/.bashrc` for persistence

### Permission denied errors

Try:
```bash
chmod +x /path/to/python/bin/python3
chmod -R +x /path/to/python/bin/
```

### Import errors for built-in modules

This usually means:
- Python installation is incomplete
- PYTHONPATH is incorrect
- Files were corrupted during extraction

Try re-extracting the tarball.

### SSL certificate errors

If you get SSL errors:
```bash
python3 -m pip install --upgrade certifi
```

Or:
```bash
python3 -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name
```

### Package installation fails

Common causes:
- Package requires compilation but build tools are missing
- Package is incompatible with Android
- Network connectivity issues

Solutions:
- Install build tools: `pkg install clang`
- Look for Android-specific versions
- Check package documentation for Android support

### Python crashes or segfaults

This could indicate:
- Incompatible architecture (verify you have ARM64)
- Corrupted installation (re-extract)
- Incompatible C extension (try different package version)
- System resource limitations

## Performance

### Is Python on Android slower than on desktop?

Performance depends on:
- Your device's processor
- Available RAM
- Thermal throttling
- Background processes

Generally, Python on modern Android devices performs adequately for most tasks.

### How can I improve performance?

Tips:
- Close unnecessary apps
- Ensure device isn't overheating
- Use efficient algorithms
- Consider using PyPy builds for compute-intensive tasks
- Profile your code to find bottlenecks

## Development

### Can I develop Android apps with this?

Python itself doesn't create native Android apps. However, you can:
- Use frameworks like Kivy or BeeWare
- Create web apps with Flask/Django
- Write automation scripts
- Develop command-line tools

### How do I debug Python code on Android?

You can use:
- Standard Python debugger (pdb)
- Print debugging
- Logging module
- IDE with remote debugging (like VS Code with remote SSH)

### Can I connect to this Python from my computer?

Yes, you can:
- Use SSH (install OpenSSH in Termux)
- Use ADB port forwarding
- Run Jupyter notebooks and connect from browser
- Use VS Code Remote Development

## Updates

### How do I update Python?

Currently:
1. Download the new version from Sacred Smoke
2. Extract to a new location or overwrite existing installation
3. Reinstall pip packages if needed

### Will my pip packages survive updates?

If you install to custom locations (not within Python directory):
```bash
python3 -m pip install --user package-name
```

Packages will be in `~/.local/lib/python3.14/` and survive updates.

### How often is Sacred Smoke updated?

Updates follow Python release cycles and when:
- Security patches are needed
- Bug fixes are available
- New features are added

## Security

### Is it safe to use?

Yes, Sacred Smoke provides official Python builds. However:
- Download only from official Sacred Smoke repository
- Verify file integrity if possible
- Be cautious with packages you install
- Follow Python security best practices

### Can I use this for production applications?

You can, but consider:
- Mobile devices have limitations (battery, resources)
- Ensure proper error handling
- Implement logging and monitoring
- Test thoroughly on target devices
- Have contingency plans for failures

## Contributing

### How can I contribute to Sacred Smoke?

See [CONTRIBUTING.md](CONTRIBUTING.md) for details. You can:
- Report bugs
- Suggest improvements
- Submit documentation fixes
- Share usage examples
- Help other users

### I found a bug, where do I report it?

Open an issue on [GitHub Issues](https://github.com/scaredsmoke-star/Sacred-smoke/issues) with:
- Detailed description
- Steps to reproduce
- Expected vs actual behavior
- Your environment details
- Relevant logs or error messages

## Additional Resources

### Where can I learn more about Python?

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python for Everybody](https://www.py4e.com/)
- [Automate the Boring Stuff](https://automatetheboringstuff.com/)

### Where can I get help?

- [GitHub Issues](https://github.com/scaredsmoke-star/Sacred-smoke/issues)
- [Python Discord](https://discord.gg/python)
- [r/learnpython](https://www.reddit.com/r/learnpython/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

---

**Didn't find your answer?** Open an issue on GitHub or check the documentation!
