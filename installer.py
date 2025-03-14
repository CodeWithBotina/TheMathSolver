import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from src.installer.license_window import LicenseWindow
from src.installer.install_window import InstallWindow

def main():
    app = QApplication(sys.argv)

    # Show the license window
    license_window = LicenseWindow()
    if license_window.exec() == QDialog.DialogCode.Accepted:
        # Show the installation window
        install_window = InstallWindow()
        if install_window.exec() == QDialog.DialogCode.Accepted:
            QMessageBox.information(None, "Installation Complete", "The application has been installed successfully.")

if __name__ == "__main__":
    main()