import sqlite3

def init_db():
    """
    Initialize the database and create necessary tables if they don't exist.
    """
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        dob TEXT NOT NULL,
        account_number TEXT UNIQUE NOT NULL,
        account_type TEXT NOT NULL,
        balance REAL DEFAULT 0
    )""")
    conn.commit()
    conn.close()

def get_db_connection():
    """
    Create and return a database connection.
    """
    return sqlite3.connect('banking_system.db')
