from PyQt6.QtWidgets import QMessageBox
from mathsolver.logic.database import (
    initialize_database, create_chat, save_message, load_chats, load_chat_messages, delete_chat
)
from mathsolver.logic.message_formats import (
    USER_MESSAGE_TEMPLATE,
    SYSTEM_MESSAGE_TEMPLATE,
    SYSTEM_ERROR_TEMPLATE,
    SYSTEM_UNSUPPORTED_TEMPLATE,
)

class ChatHandler:
    def __init__(self):
        """Initialize the chat handler and the database."""
        initialize_database()

    def create_chat(self, name, operation_type):
        """Create a new chat and return its ID."""
        return create_chat(name, operation_type)

    def save_message(self, chat_id, sender, message):
        """Save a message to the database."""
        save_message(chat_id, sender, message)

    def load_chats(self, chat_selector):
        """Load all chats and populate the chat selector."""
        chats = load_chats()
        chat_selector.clear()
        for chat_id, name, operation_type in chats:
            chat_selector.addItem(f"{name} ({operation_type})", chat_id)

    def load_chat_messages(self, chat_id):
        """Load all messages for a specific chat."""
        return load_chat_messages(chat_id)

    def delete_chat(self, chat_id):
        """Delete a chat and its messages from the database."""
        delete_chat(chat_id)

    def start_chat(self, window):
        """Handle the chat interface after sending the formula."""
        formula = window.formula_input.text().strip()

        if not formula:
            QMessageBox.warning(window, "Error", "Please enter a formula before sending.")
            return

        if not window.selected_operation:
            QMessageBox.warning(window, "Error", "Please select an operation type before sending.")
            return

        # Hide the title
        window.title_label.hide()

        # User message (aligned to the left)
        user_message = USER_MESSAGE_TEMPLATE.format(
            operation=window.selected_operation,
            formula=formula
        )

        # Handle induction problems
        if window.selected_operation == "Induction":
            try:
                induction_handler = InductionHandler(formula)
                solution = induction_handler.solve_induction()
                app_response = SYSTEM_MESSAGE_TEMPLATE.format(solution=solution)
            except Exception as e:
                app_response = SYSTEM_ERROR_TEMPLATE.format(error=str(e))
        else:
            app_response = SYSTEM_UNSUPPORTED_TEMPLATE

        # Append messages to chat_display
        window.chat_display.append(user_message)
        window.chat_display.append(app_response)
        window.formula_input.clear()