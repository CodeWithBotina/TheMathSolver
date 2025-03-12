# mathsolver/logic/chat_handler.py

from mathsolver.modules.induction import InductionHandler  # Ensure the import is correct
from PyQt6.QtWidgets import QMessageBox
from mathsolver.logic.message_formats import (  # Import the message templates
    USER_MESSAGE_TEMPLATE,
    SYSTEM_MESSAGE_TEMPLATE,
    SYSTEM_ERROR_TEMPLATE,
    SYSTEM_UNSUPPORTED_TEMPLATE,
)

def start_chat(window):
    """Handles the chat interface after sending the formula."""
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