import sqlite3
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
        acc_type = input("Choose account type (Personal/Business): ").strip().capitalize()

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
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def authenticate_user():
    """
    Authenticate an existing user and direct them to banking operations.
    """
    from services.bank_service import perform_operations

    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
        return

    if user:
        print(f"Welcome back, {user[3]}!")
        perform_operations(user)
    else:
        print("Invalid username or password. Please try again.")
