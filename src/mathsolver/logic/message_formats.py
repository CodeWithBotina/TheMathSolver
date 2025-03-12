# mathsolver/logic/message_formats.py

# Template for user messages
USER_MESSAGE_TEMPLATE = """
<div class="user-message">
    <b>You ({operation}):</b> {formula}
</div>
"""

# Template for system messages (step-by-step solution)
SYSTEM_MESSAGE_TEMPLATE = """
<div class="system-message">
    <b>MathSolver:</b> Here's the step-by-step solution:<br><br>
    {solution}
</div>
"""

# Template for system messages (error)
SYSTEM_ERROR_TEMPLATE = """
<div class="system-message">
    <b>MathSolver:</b> Error processing the formula: {error}
</div>
"""

# Template for system messages (unsupported operation)
SYSTEM_UNSUPPORTED_TEMPLATE = """
<div class="system-message">
    <b>MathSolver:</b> Operation not supported yet.
</div>
"""