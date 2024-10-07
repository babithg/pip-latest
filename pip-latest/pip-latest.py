import subprocess
import sys

def upgrade_pip():
    """Upgrade pip to the latest version."""
    try:
        # Run the command to upgrade pip
        print("Upgrading pip to the latest version...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("pip has been successfully upgraded.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade pip: {e}")
        sys.exit(1)

def main():
    upgrade_pip()

if __name__ == "__main__":
    main()
