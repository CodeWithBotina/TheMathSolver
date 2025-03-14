import os
import sys
from functools import partial
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QMenu, QTextEdit, QLabel,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox, QComboBox
)
from PyQt6.QtGui import QAction
from mathsolver.logic.ui_loader import load_ui_file
from mathsolver.logic.about_handler import show_about
from mathsolver.logic.chat_handler import ChatHandler
from mathsolver.logic.formula_handler import FormulaHandler
from mathsolver.ui.style.styles import load_styles
from mathsolver.ui.style.icon import get_window_icon  # Import the icon function

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize handlers
        self.chat_handler = ChatHandler()
        self.formula_handler = FormulaHandler()

        # Get base directory
        if getattr(sys, 'frozen', False):
            # If the application is packaged, use the temporary path from PyInstaller
            base_dir = sys._MEIPASS
        else:
            # If not packaged, use the normal path
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        # Construct the path to the UI file
        ui_path = os.path.join(base_dir, "mathsolver", "ui", "main_window.ui")
        
        # Debug: Print the resolved path
        print(f"Base directory: {base_dir}")
        print(f"UI path: {ui_path}")

        # Check if the UI file exists
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")

        # Load the UI
        load_ui_file(self, ui_path)

        # Set the window icon
        try:
            self.setWindowIcon(get_window_icon())
        except FileNotFoundError as e:
            print(e)  # Log the error if the icon file is not found

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
        self.chat_selector = self.findChild(QComboBox, "chatSelector")  # Get the QComboBox
        self.delete_button = QPushButton("Delete Chat", self)  # Add delete button

        # Button "New Chat"
        self.new_chat_button = QPushButton("New Chat", self)
        self.new_chat_button.clicked.connect(self.create_temp_chat)

        # Initialize temporary chat
        self.temp_chat = None  # Temporary chat not created at startup

        # Dropdown menu for operations
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
        load_styles(self)
        
        # Connect events
        self.setup_events()

        # Initialize chat system
        self.current_chat_id = None
        self.load_chats()

    def create_temp_chat(self):
        """Create a new temporary chat."""
        # Clear the chat area
        self.chat_display.clear()

        # Set the temporary chat
        self.temp_chat = {
            "name": "New Chat",
            "operation_type": self.selected_operation or "Sets",
        }

        # Update the chat selector
        self.chat_selector.addItem("New Chat", -1)  # Use -1 as a temporary ID
        self.chat_selector.setCurrentIndex(self.chat_selector.count() - 1)

        # Reset the current chat ID
        self.current_chat_id = None

    def set_operation(self, text):
        """Store the selected operation and update the button."""
        self.selected_operation = text
        self.button.setText(text)

    def setup_layout(self):
        """Set up the layout of the widgets."""
        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)

        # Add widgets to the layout
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.chat_selector)  # Add chat selector
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.chat_display)
        self.layout.addWidget(self.image_label)  # Add label for displaying images

        # Input layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.formula_input)
        input_layout.addWidget(self.send_button)
        self.layout.addLayout(input_layout)

        # Buttons "New Chat" and "Delete Chat" in a QHBoxLayout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.new_chat_button)  # Button "New Chat"
        button_layout.addWidget(self.delete_button)    # Button "Delete Chat"

        # Adjust button size to occupy half the space
        button_layout.setStretch(0, 1)  # "New Chat" occupies half
        button_layout.setStretch(1, 1)  # "Delete Chat" occupies the other half

        self.layout.addLayout(button_layout)  # Add button layout to the main layout

    def setup_events(self):
        """Set up interface events."""
        self.send_button.clicked.connect(lambda: self.process_formula())
        self.chat_selector.currentIndexChanged.connect(self.switch_chat)  # Event for chat selection
        self.delete_button.clicked.connect(self.delete_current_chat)  # Event for deleting chat

        about_action = self.findChild(QAction, "actionAbout")
        if about_action:
            about_action.triggered.connect(lambda: show_about(self))

    def load_chats(self):
        """Load all chats and populate the chat selector."""
        self.chat_handler.load_chats(self.chat_selector)

    def switch_chat(self):
        """Switch to the selected chat and load its messages."""
        chat_id = self.chat_selector.currentData()
        if chat_id:
            self.current_chat_id = chat_id
            self.load_chat_messages()

    def load_chat_messages(self):
        """Load and display the messages for the current chat."""
        self.chat_display.clear()
        messages = self.chat_handler.load_chat_messages(self.current_chat_id)
        for sender, message, timestamp in messages:
            if sender == 'user':
                self.chat_display.append(f"""
                <div class="user-message">
                    <b>You:</b> {message}
                </div>
                """)
            else:
                self.chat_display.append(f"""
                <div class="system-message">
                    <b>MathSolver:</b> {message}
                </div>
                """)

    def delete_current_chat(self):
        """Delete the currently selected chat."""
        if self.current_chat_id is None:
            QMessageBox.warning(self, "Error", "No chat selected to delete.")
            return

        reply = QMessageBox.question(self, 'Delete Chat', 'Are you sure you want to delete this chat?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.chat_handler.delete_chat(self.current_chat_id)
            self.load_chats()

            # Check if there are no chats left
            if self.chat_selector.count() == 0:
                # Reset the current chat ID and clear the chat display
                self.current_chat_id = None
                self.chat_display.clear()
            else:
                # Switch to the first chat in the list
                self.chat_selector.setCurrentIndex(0)
                self.current_chat_id = self.chat_selector.currentData()
                self.load_chat_messages()

    def process_formula(self):
        """Process the formula based on the selected operation."""
        formula = self.formula_input.text().strip()
        if not formula:
            QMessageBox.warning(self, "Error", "Please enter a formula.")
            return

        if not self.selected_operation:
            QMessageBox.warning(self, "Error", "Please select an operation type.")
            return

        # If it's a temporary chat, save it to the database
        if self.temp_chat is not None:
            # Create a new chat in the database
            chat_name = formula[:50]  # Use the formula as the chat name
            self.current_chat_id = self.chat_handler.create_chat(chat_name, self.selected_operation)
            self.temp_chat = None  # Remove the temporary chat state

            # Update the chat selector
            self.load_chats()
            self.chat_selector.setCurrentIndex(self.chat_selector.count() - 1)

        # If there is no current chat, create a new one
        if self.current_chat_id is None:
            chat_name = formula[:50]  # Use the formula as the chat name
            self.current_chat_id = self.chat_handler.create_chat(chat_name, self.selected_operation)
            self.load_chats()
            self.chat_selector.setCurrentIndex(self.chat_selector.count() - 1)

        # Save the user's message
        user_message = f"""
        <div class="user-message">
            <b>You ({self.selected_operation}):</b> {formula}
        </div>
        """
        self.chat_display.append(user_message)
        self.chat_handler.save_message(self.current_chat_id, 'user', formula)

        # Process the formula and get the response
        app_response = self.formula_handler.process_formula(self.selected_operation, formula)
        self.chat_display.append(app_response)
        self.chat_handler.save_message(self.current_chat_id, 'system', app_response)

        # Clear the input field
        self.formula_input.clear()