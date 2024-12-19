import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from db.database import get_db_connection
from utils.account_utils import generate_account_number


import getpass
from db.database import get_db_connection
from utils.account_utils import generate_account_number

def register_new_user():
    """
    Register a new user in the system.
    """
    try:
        name = input("Enter your full name: ")
        dob = input("Enter your Date of Birth (DD/MM/YYYY): ")
        username = input("Create a username: ")
        password = getpass.getpass("Create a password: ")
        acc_type = input("Choose account type (Personal/Business): ").capitalize()

        if acc_type not in ["Personal", "Business"]:
            print("Invalid account type. Please choose either Personal or Business.")
            return

        account_number = generate_account_number()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO users (username, password, name, dob, account_number, account_type, balance)
        VALUES (?, ?, ?, ?, ?, ?, 0)""",
                       (username, password, name, dob, account_number, acc_type))
        conn.commit()
        conn.close()

        print(f"Account created successfully! Your account number is: {account_number}")
    except sqlite3.IntegrityError:
        print("Username or account number already exists. Please try again.")

def authenticate_user():
    """
    Authenticate an existing user and direct them to banking operations.
    """
    from services.bank_service import perform_operations

    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"Welcome back, {user[3]}!")
        perform_operations(user)
    else:
        print("Invalid username or password. Please try again.")
