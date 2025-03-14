import sys
import os

# Añade la carpeta raíz del proyecto a sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(project_root)

from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from src.installer.license_window import LicenseWindow
from src.installer.install_window import InstallWindow

def main():
    app = QApplication(sys.argv)

    # Show license window
    license_window = LicenseWindow()
    if license_window.exec() == QDialog.DialogCode.Accepted:
        # Show installation window
        install_window = InstallWindow()
        if install_window.exec() == QDialog.DialogCode.Accepted:
            QMessageBox.information(None, "Installation Complete", "The application has been installed successfully.")

if __name__ == "__main__":
    main()