from PyQt6.QtWidgets import QMessageBox

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

    # User message
    user_message = f"""
    <div style='background-color: #4a4a6a; padding: 10px; border-radius: 10px; 
                margin: 5px 0; color: white; text-align: right; 
                max-width: 70%; float: right; clear: both;'>
        <b>You ({window.selected_operation}):</b> {formula}
    </div>
    """

    # Application response
    app_response = f"""
    <div style='background-color: #3a3a5a; padding: 10px; border-radius: 10px; 
                margin: 5px 0; color: white; text-align: left;'>
        <b>MathSolver: Hello, how are you?</b>
    </div>
    """

    # Append messages to chat_display
    window.chat_display.append(user_message)
    window.chat_display.append(app_response)
    window.formula_input.clear()