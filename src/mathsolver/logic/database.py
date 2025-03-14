import sqlite3
from datetime import datetime
import os
import sys

def get_project_root():
    """Get the absolute path to the project root directory."""
    if getattr(sys, 'frozen', False):
        # If the script is packaged (e.g., by PyInstaller), use the executable's directory
        return os.path.dirname(sys.executable)
    # Otherwise, use the directory of this script
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_data_dir():
    """Get the path to the .data directory in the project root."""
    project_root = get_project_root()
    data_dir = os.path.join(project_root, ".data")
    os.makedirs(data_dir, exist_ok=True)  # Create the .data directory if it doesn't exist
    return data_dir

# Full path to the database in the .data folder
DATABASE_PATH = os.path.join(get_data_dir(), "chat_history.db")

def initialize_database():
    """Initialize the database and create the necessary tables if they don't exist."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Create the chats table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,  -- Chat name (first operation entered)
            operation_type TEXT NOT NULL,  -- Operation type (Sets, Functions, etc.)
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP  -- Chat creation date
        )
    ''')

    # Create the messages table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,  -- ID of the chat the message belongs to
            sender TEXT NOT NULL,  -- "user" or "system"
            message TEXT NOT NULL,  -- Message content
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Message timestamp
            FOREIGN KEY (chat_id) REFERENCES chats (id)
        )
    ''')

    conn.commit()
    conn.close()

def create_chat(name, operation_type):
    """Create a new chat and return its ID."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO chats (name, operation_type) VALUES (?, ?)
    ''', (name, operation_type))
    chat_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return chat_id

def save_message(chat_id, sender, message):
    """Save a message to the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (chat_id, sender, message) VALUES (?, ?, ?)
    ''', (chat_id, sender, message))
    conn.commit()
    conn.close()

def load_chats():
    """Load all chats from the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, operation_type FROM chats ORDER BY created_at')
    chats = cursor.fetchall()
    conn.close()
    return chats

def load_chat_messages(chat_id):
    """Load all messages for a specific chat."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT sender, message, timestamp FROM messages
        WHERE chat_id = ?
        ORDER BY timestamp
    ''', (chat_id,))
    messages = cursor.fetchall()
    conn.close()
    return messages

def delete_chat(chat_id):
    """Delete a chat and its messages from the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM chats WHERE id = ?', (chat_id,))
    cursor.execute('DELETE FROM messages WHERE chat_id = ?', (chat_id,))
    conn.commit()
    conn.close()