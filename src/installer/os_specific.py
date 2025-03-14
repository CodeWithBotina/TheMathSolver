import os
import platform
import shutil
import subprocess

def get_default_install_path():
    """Get the default installation path based on the operating system."""
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.environ.get("ProgramFiles", "C:\\Program Files"), "MathSolver")
    elif system == "Linux":
        if os.geteuid() == 0:  # Running as root
            return "/opt/mathsolver"
        else:
            return os.path.join(os.path.expanduser("~"), ".mathsolver")
    elif system == "Darwin":  # macOS
        return "/Applications/MathSolver.app"
    else:
        raise OSError(f"Unsupported operating system: {system}")

def create_hidden_data_folder(install_path):
    """Create a hidden .data folder in the installation directory."""
    data_dir = os.path.join(install_path, ".data")
    os.makedirs(data_dir, exist_ok=True)

    # Hide the folder on Windows
    if platform.system() == "Windows":
        import ctypes
        ctypes.windll.kernel32.SetFileAttributesW(data_dir, 2)  # 2 is the hidden attribute

def create_shortcut(install_path, create_shortcut=True):
    """Create a shortcut to the application."""
    system = platform.system()
    if system == "Windows":
        if create_shortcut:
            import winshell
            from win32com.client import Dispatch
            desktop = winshell.desktop()
            path = os.path.join(desktop, "MathSolver.lnk")
            target = os.path.join(install_path, "MathSolver.exe")
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = install_path
            shortcut.save()
    elif system == "Linux":
        if create_shortcut:
            if os.geteuid() == 0:  # Running as root
                desktop_file = "/usr/share/applications/mathsolver.desktop"
            else:
                desktop_file = os.path.join(os.path.expanduser("~"), ".local", "share", "applications", "mathsolver.desktop")
            
            # Create the folder if it doesn't exist
            os.makedirs(os.path.dirname(desktop_file), exist_ok=True)
            
            with open(desktop_file, "w") as f:
                f.write(f"""
                [Desktop Entry]
                Name=MathSolver
                Exec={os.path.join(install_path, "mathsolver")}
                Icon={os.path.join(install_path, "assets", "icons", "icon.png")}
                Type=Application
                """)
    elif system == "Darwin":
        if create_shortcut:
            app_path = os.path.join(install_path, "MathSolver.app")
            os.makedirs(app_path, exist_ok=True)
            # Add logic to create a macOS shortcut