import os
import sys

def load_styles(window):
    """Load styles from an external file."""
    if getattr(sys, 'frozen', False):
        # If the application is packaged, use the temporary path from PyInstaller
        base_dir = sys._MEIPASS
    else:
        # If not packaged, use the normal path
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Construct the path to the stylesheet
    style_path = os.path.join(base_dir, "mathsolver", "ui", "style", "main_window.qss")
    
    # Check if the stylesheet exists
    if os.path.exists(style_path):
        with open(style_path, "r") as file:
            window.setStyleSheet(file.read())
    else:
        # If the stylesheet is not found, try an alternative path (for packaged apps)
        style_path = os.path.join(base_dir, "ui", "style", "main_window.qss")
        if os.path.exists(style_path):
            with open(style_path, "r") as file:
                window.setStyleSheet(file.read())
        else:
            raise FileNotFoundError(f"Stylesheet not found: {style_path}")