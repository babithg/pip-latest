# pip-latest

A simple CLI tool to upgrade pip to its latest version or check if an update is available.

---

## Installation

Install from [PyPI](https://pypi.org/project/pip_latest/):

```bash
pip install pip-latest
```

---

## Source Code

Available on GitHub: [https://github.com/babithg/pip-latest](https://github.com/babithg/pip-latest)

---

## Usage

### Upgrade pip to the latest version

```bash
pip-latest get
```

Upgrades pip and prints the new version on success.

### Check if a newer version is available

```bash
pip-latest check
```

Compares your currently installed pip version against the latest release on PyPI and tells you if an update is available.

### Show help

```bash
pip-latest help
```

---

## Commands

| Command | Description |
|---------|-------------|
| `get`   | Upgrade pip to the latest version |
| `check` | Check if a newer version of pip is available |
| `help`  | Show usage help |

---

## License

MIT — see [LICENSE](LICENSE) for details.
