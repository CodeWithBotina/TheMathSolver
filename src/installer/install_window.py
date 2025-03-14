import os
import shutil
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QFileDialog, QMessageBox
from .os_specific import get_default_install_path, create_hidden_data_folder, create_shortcut
import platform
import subprocess

class InstallWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Installation")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.folder_label = QLabel("Select installation folder:")
        layout.addWidget(self.folder_label)

        self.folder_input = QLineEdit()
        self.folder_input.setText(get_default_install_path())
        layout.addWidget(self.folder_input)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_folder)
        layout.addWidget(browse_button)

        self.create_shortcut_checkbox = QCheckBox("Create a desktop shortcut")
        self.create_shortcut_checkbox.setChecked(True)
        layout.addWidget(self.create_shortcut_checkbox)

        self.launch_app_checkbox = QCheckBox("Launch application after installation")
        self.launch_app_checkbox.setChecked(True)
        layout.addWidget(self.launch_app_checkbox)

        install_button = QPushButton("Install")
        install_button.clicked.connect(self.start_installation)
        layout.addWidget(install_button)

        self.setLayout(layout)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Installation Directory")
        if folder:
            self.folder_input.setText(folder)

    def start_installation(self):
        folder = self.folder_input.text()
        if not folder:
            QMessageBox.warning(self, "Error", "Please select an installation folder.")
            return

        try:
            # Create the installation directory
            os.makedirs(folder, exist_ok=True)

            # Get the path to the compiled executable
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            source_dir = os.path.join(base_dir, "dist")

            # Copy the executable and necessary files
            for item in os.listdir(source_dir):
                s = os.path.join(source_dir, item)
                d = os.path.join(folder, item)

                if os.path.exists(d):
                    if os.path.isfile(d):
                        os.remove(d)
                    elif os.path.isdir(d):
                        shutil.rmtree(d)

                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)

            # Create the hidden .data folder
            create_hidden_data_folder(folder)

            # Create a shortcut if enabled
            create_shortcut(folder, self.create_shortcut_checkbox.isChecked())

            QMessageBox.information(self, "Success", f"Application installed successfully in {folder}")

            # Launch the application if enabled
            if self.launch_app_checkbox.isChecked():
                if platform.system() == "Windows":
                    subprocess.Popen([os.path.join(folder, "MathSolver.exe")])
                else:
                    subprocess.Popen([os.path.join(folder, "mathsolver")])

            self.accept()
        except PermissionError:
            QMessageBox.critical(self, "Permission Denied", "You do not have permission to install in this location. Please choose a different folder or run the installer as root.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred during installation: {e}")