import os
import platform
import subprocess
import sys

def build_windows():
    """Build the executable for Windows."""
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=MathSolver",
        "--icon=assets/icons/icon.ico",
        "--add-data=src/mathsolver/about/about.json;about",
        "--add-data=src/mathsolver/about/LICENSE.json;about",
        "--add-data=src/mathsolver/ui/style/main_window.qss;ui/style",
        "src/mathsolver/main.py"
    ])

def build_linux():
    """Build the executable for Linux."""
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--name=mathsolver",
        "--add-data=src/mathsolver/about/about.json:about",
        "--add-data=src/mathsolver/about/LICENSE.json:about",
        "--add-data=src/mathsolver/ui/style/main_window.qss:ui/style",
        "src/mathsolver/main.py"
    ])

def build_mac():
    """Build the executable for macOS."""
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=MathSolver",
        "--icon=assets/icons/icon.icns",
        "--add-data=src/mathsolver/about/about.json:about",
        "--add-data=src/mathsolver/about/LICENSE.json:about",
        "--add-data=src/mathsolver/ui/style/main_window.qss:ui/style",
        "src/mathsolver/main.py"
    ])

def main():
    system = platform.system()
    if system == "Windows":
        build_windows()
    elif system == "Linux":
        build_linux()
    elif system == "Darwin":
        build_mac()
    else:
        print(f"Unsupported platform: {system}")

if __name__ == "__main__":
    main()