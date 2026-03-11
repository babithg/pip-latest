import subprocess
import sys
import json
import urllib.request


def get_current_pip_version():
    """Get the currently installed pip version."""
    result = subprocess.check_output(
        [sys.executable, "-m", "pip", "--version"],
        text=True
    )
    # Output: "pip 23.1.2 from /path ..."
    return result.split()[1]


def get_latest_pip_version():
    """Fetch the latest pip version from PyPI."""
    url = "https://pypi.org/pypi/pip/json"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    return data["info"]["version"]


def cmd_get():
    """Upgrade pip to the latest version."""
    try:
        print("Upgrading pip to the latest version...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        new_version = get_current_pip_version()
        print(f"pip successfully upgraded  →  {new_version}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade pip: {e}")
        sys.exit(1)


def cmd_check():
    """Check if a newer version of pip is available."""
    try:
        current = get_current_pip_version()
        latest  = get_latest_pip_version()

        print(f"Installed : {current}")
        print(f"Latest    : {latest}")

        if current == latest:
            print("pip is already up to date.")
        else:
            print(f"Update available!  {current}  →  {latest}")
            print("Run  'pip-latest get'  to upgrade.")
    except Exception as e:
        print(f"Failed to check pip version: {e}")
        sys.exit(1)


def cmd_help():
    """Print usage/syntax help."""
    help_text = """
Usage:
  pip-latest <command>

Commands:
  get     Upgrade pip to the latest version
  check   Check if a newer version of pip is available
  help    Show this help message

Examples:
  pip-latest get
  pip-latest check
  pip-latest help
"""
    print(help_text)


def main():
    commands = {
        "get"  : cmd_get,
        "check": cmd_check,
        "help" : cmd_help,
    }

    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print(f"Error: Invalid or missing command.")
        cmd_help()
        sys.exit(1)

    commands[sys.argv[1]]()


if __name__ == "__main__":
    main()