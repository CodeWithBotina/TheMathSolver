import os
import sys
from PyQt6.QtGui import QIcon

def get_icon_path():
    """Determine the correct icon path based on the operating system."""
    if getattr(sys, 'frozen', False):
        # If the application is packaged, use the temporary path from PyInstaller
        base_dir = sys._MEIPASS
    else:
        # If not packaged, use the normal path
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

    # Determine the icon format based on the operating system
    system = sys.platform
    if system == "win32":
        icon_file = "icon.ico"  # Windows uses .ico files
    elif system == "darwin":
        icon_file = "icon.icns"  # macOS uses .icns files
    else:
        icon_file = "icon.png"  # Linux and other systems use .png files

    # Construct the path to the icon file
    icon_path = os.path.join(base_dir, "mathsolver", "assets", "icons", icon_file)
    
    # Debug: Print the resolved path
    print(f"Base directory: {base_dir}")
    print(f"Icon path: {icon_path}")

    # Check if the icon file exists
    if not os.path.exists(icon_path):
        raise FileNotFoundError(f"Icon file not found: {icon_path}")

    return icon_path

def get_window_icon():
    """Get the QIcon object for the window icon."""
    icon_path = get_icon_path()
    return QIcon(icon_path)