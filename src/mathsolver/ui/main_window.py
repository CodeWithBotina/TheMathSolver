import os
import sys
import tempfile
import matplotlib.pyplot as plt
from functools import partial
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMenu, QTextEdit, QLabel,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox
)
from PyQt6.QtGui import QAction, QPixmap
from mathsolver.logic.ui_loader import load_ui_file
from mathsolver.logic.chat_handler import start_chat
from mathsolver.logic.about_handler import show_about
from mathsolver.modules.induction import InductionHandler  # Import the induction module

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Get UI elements
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("background-color: #2d2d2d; color: white;")

        # Get base directory
        if getattr(sys, 'frozen', False):
            base_dir = sys._MEIPASS
        else:
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
        self.image_label = QLabel(self)  # Label to display generated images
        
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
        self.layout.addWidget(self.chat_display)
        self.layout.addWidget(self.image_label)  # Add label for displaying images

        # Input layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.formula_input)
        input_layout.addWidget(self.send_button)
        self.layout.addLayout(input_layout)

    def load_styles(self):
        """Load styles from an external file."""
        if getattr(sys, 'frozen', False):
            base_dir = sys._MEIPASS
        else:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        style_path = os.path.join(base_dir, "mathsolver", "ui", "style", "main_window.qss")
        if os.path.exists(style_path):
            with open(style_path, "r") as file:
                self.setStyleSheet(file.read())
        else:
            raise FileNotFoundError(f"Stylesheet not found: {style_path}")

    def setup_events(self):
        """Set up interface events."""
        self.send_button.clicked.connect(lambda: self.process_formula())

        about_action = self.findChild(QAction, "actionAbout")
        if about_action:
            about_action.triggered.connect(lambda: show_about(self))

    def set_operation(self, text):
        """Store the selected operation and update the button."""
        self.selected_operation = text
        self.button.setText(text)

    def process_formula(self):
        """Process the formula based on the selected operation."""
        formula = self.formula_input.text().strip()
        if not formula:
            QMessageBox.warning(self, "Error", "Please enter a formula.")
            return

        if not self.selected_operation:
            QMessageBox.warning(self, "Error", "Please select an operation type.")
            return

        # User message (aligned to the right)
        user_message = f"""
        <div class="user-message">
            <b>You ({self.selected_operation}):</b> {formula}
        </div>
        """
        self.chat_display.append(user_message)

        # Handle induction problems
        if self.selected_operation == "Induction":
            try:
                induction_handler = InductionHandler(formula)
                solution = induction_handler.solve_induction()
                app_response = f"""
                <div class="system-message">
                    {solution}
                </div>
                """
            except Exception as e:
                app_response = f"""
                <div class="system-message">
                    <b>MathSolver:</b> Error processing the formula: {e}
                </div>
                """
        else:
            app_response = f"""
            <div class="system-message">
                <b>MathSolver:</b> Operation not supported yet.
            </div>
            """

        # Append the response to the chat
        self.chat_display.append(app_response)
        self.formula_input.clear()