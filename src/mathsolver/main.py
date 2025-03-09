import sys
import os
from PyQt6.QtWidgets import QApplication

# Add the root directory (MathSolver/) to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(root_dir)

# Now you can import from assets
from mathsolver.ui.main_window import MainWindow

def main():
    """Entry point for the application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()