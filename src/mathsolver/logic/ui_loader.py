import os
import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMessageBox

def load_ui_file(window, ui_path):
    """Loads the UI from the .ui file."""
    if not os.path.exists(ui_path):
        print(f"Error: UI file not found at {ui_path}")
        QMessageBox.critical(window, "Error", "UI file not found.")
        sys.exit(1)
    
    try:
        loadUi(ui_path, window)
    except Exception as e:
        print(f"Error loading .ui file: {e}")
        QMessageBox.critical(window, "Error", "There was a problem loading the UI.")
        sys.exit(1)