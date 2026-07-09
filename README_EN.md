# py-clipboard-manager 📋

Cross-platform clipboard history manager.

## Quick Start

### Install Dependencies

> ⚠️ Use `python3 -m pip install` to ensure correct Python environment.

```bash
python3 -m pip install pyperclip
```

### Usage

```bash
# List recent 10 items
python3 clipboard.py -l

# Copy item #3 to clipboard
python3 clipboard.py -c 3

# Clear history
python3 clipboard.py --clear

# Start daemon mode (auto-save)
python3 clipboard.py --daemon
```

## Supported Platforms

- macOS
- Windows
- Linux

## License

MIT
