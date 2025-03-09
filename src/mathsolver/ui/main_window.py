import os
import sys
from functools import partial
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QMessageBox, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
from PyQt6.QtGui import QAction
from mathsolver.logic.ui_loader import load_ui_file
from mathsolver.logic.chat_handler import start_chat
from mathsolver.logic.about_handler import show_about

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Get UI elements
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("background-color: #2d2d2d; color: white;")

        # Get the absolute path to the assets directory
        if getattr(sys, 'frozen', False):
            # If the application is packaged, use the temporary path from PyInstaller
            base_dir = sys._MEIPASS
        else:
            # If not packaged, use the normal path
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        assets_dir = os.path.join(base_dir, "mathsolver")

        # Load the UI
        ui_path = os.path.join(assets_dir, "ui", "main_window.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        load_ui_file(self, ui_path)

        # Adjust size
        self.resize(800, 600)

        # Get UI elements
        self.button = self.findChild(QPushButton, "selectionButton")
        self.send_button = self.findChild(QPushButton, "sendButton")
        self.title_label = self.findChild(QLabel, "titleLabel")
        self.formula_input = self.findChild(QLineEdit, "formulaInput")
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)

        # Dropdown menu
        self.menu = QMenu(self)
        options = ["Sets", "Functions", "Relations", "Induction"]
        self.selected_operation = None

        for option in options:
            action = self.menu.addAction(option)
            action.triggered.connect(partial(self.set_operation, option))

        self.button.setMenu(self.menu)

        # Set up layout
        self.setup_layout()

        # Load styles
        self.load_styles()

        # Connect events
        self.setup_events()

    def setup_layout(self):
        """Set up the layout of the widgets."""
        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)

        # Add widgets to the layout
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.chat_display)  # Ensure chat_display is added

        # Input layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.formula_input)
        input_layout.addWidget(self.send_button)
        self.layout.addLayout(input_layout)

    def load_styles(self):
        """Load styles from an external file."""
        if getattr(sys, 'frozen', False):
            # If the application is packaged, use the temporary path from PyInstaller
            base_dir = sys._MEIPASS
        else:
            # If not packaged, use the normal path
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        style_path = os.path.join(base_dir, "mathsolver", "ui", "style", "main_window.qss")
        if os.path.exists(style_path):
            with open(style_path, "r") as file:
                self.setStyleSheet(file.read())
        else:
            raise FileNotFoundError(f"Stylesheet not found: {style_path}")

    def setup_events(self):
        """Set up interface events."""
        self.send_button.clicked.connect(lambda: start_chat(self))

        about_action = self.findChild(QAction, "actionAbout")
        if about_action:
            about_action.triggered.connect(lambda: show_about(self))

    def set_operation(self, text):
        """Store the selected operation and update the button."""
        self.selected_operation = text
        self.button.setText(text)