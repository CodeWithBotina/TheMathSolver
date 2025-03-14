import os
import sys
import json
from PyQt6.QtWidgets import QMessageBox

def show_about(window):
    """Display the 'About' window with information from a JSON file."""
    if getattr(sys, 'frozen', False):
        # If the application is packaged, use the temporary path from PyInstaller
        base_dir = sys._MEIPASS
    else:
        # If not packaged, use the normal path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construct the path to the about.json file
    about_path = os.path.join(base_dir, "about", "about.json")
    
    # Debug: Print the resolved path
    print(f"Base directory: {base_dir}")
    print(f"About path: {about_path}")

    # Check if the file exists
    if not os.path.exists(about_path):
        QMessageBox.warning(window, "Error", f"The 'about.json' file was not found at: {about_path}")
        return

    try:
        # Read the JSON file
        with open(about_path, "r", encoding="utf-8") as file:
            about_data = json.load(file)
    except Exception as e:
        QMessageBox.warning(window, "Error", f"There was a problem reading 'about.json': {e}")
        return

    # Extract information from the JSON file
    title = about_data.get("title", "About")
    description = about_data.get("description", "")
    author = about_data.get("author", "")
    year = about_data.get("year", "")
    project = about_data.get("project", "")

    # Format the message
    message = f"{description}\n\n{author}\n{year}\n{project}"

    # Display the information in a message box
    QMessageBox.information(window, title, message)