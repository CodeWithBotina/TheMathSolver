import json
import os
import sys
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QMessageBox, QTextEdit

class LicenseWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("License Agreement")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        # Load license text from JSON
        license_text = self.load_license()
        if not license_text:
            QMessageBox.critical(self, "Error", "Could not load the license agreement.")
            self.reject()

        # Display license text
        license_display = QTextEdit()
        license_display.setPlainText(license_text)
        license_display.setReadOnly(True)
        layout.addWidget(license_display)

        # Buttons
        accept_button = QPushButton("Accept")
        accept_button.clicked.connect(self.accept_license)
        layout.addWidget(accept_button)

        reject_button = QPushButton("Reject")
        reject_button.clicked.connect(self.reject_license)
        layout.addWidget(reject_button)

        self.setLayout(layout)

    def load_license(self):
        """Load the license text from the JSON file."""
        try:
            # Get the base directory depending on whether the app is packaged or not
            if getattr(sys, 'frozen', False):
                # If the app is packaged, use sys._MEIPASS
                base_dir = sys._MEIPASS
            else:
                # If not packaged, use the normal path
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            # Construct the path to the LICENSE.json file
            license_path = os.path.join(base_dir, "src", "mathsolver", "about", "LICENSE.json")
            
            with open(license_path, "r") as file:
                license_data = json.load(file)
                return license_data.get("text", "License text not found.")
        except Exception as e:
            print(f"Error loading license: {e}")
            return None

    def accept_license(self):
        QMessageBox.information(self, "Accepted", "You have accepted the license agreement.")
        self.accept()

    def reject_license(self):
        QMessageBox.warning(self, "Rejected", "You must accept the license agreement to continue.")
        self.reject()