import random
import getpass
import sqlite3

print("\nWELCOME TO THE STATE BANK OF INDIA")

# Initialize the database
def init_db():
    try:
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
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error during initialization: {e}")
    finally:
        conn.close()

# Generate a new account number
def generate_account_number():
    base_number = "314151000"
    random_part = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    return base_number + random_part

# Register a new user
def register_new_user():
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
        conn = sqlite3.connect('banking_system.db')
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO users (username, password, name, dob, account_number, account_type, balance)
        VALUES (?, ?, ?, ?, ?, ?, 0)""",
                       (username, password, name, dob, account_number, acc_type))
        conn.commit()
        print(f"Account created successfully! Your account number is: {account_number}")
    except sqlite3.IntegrityError:
        print("Username or account number already exists. Please try again.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Authenticate an existing user
def authenticate_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    try:
        conn = sqlite3.connect('banking_system.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return
    finally:
        conn.close()

    if user:
        print(f"Welcome back, {user[3]}!")
        perform_operations(user)
    else:
        print("Invalid username or password. Please try again.")

# Perform banking operations
def perform_operations(user):
    while True:
        print("\nAvailable Operations:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            deposit(user)
        elif choice == '2':
            withdraw(user)
        elif choice == '3':
            view_balance(user)
        elif choice == '4':
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Deposit money
def deposit(user):
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Invalid amount. Deposit amount must be greater than zero.")
            return

        conn = sqlite3.connect('banking_system.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET balance = balance + ? WHERE account_number = ?",
                       (amount, user[5]))
        conn.commit()
        print(f"Successfully deposited Rs. {amount:.2f}.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Withdraw money
def withdraw(user):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount. Withdrawal amount must be greater than zero.")
            return

        conn = sqlite3.connect('banking_system.db')
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM users WHERE account_number = ?", (user[5],))
        balance = cursor.fetchone()[0]

        if amount > balance:
            print("Insufficient balance. Please enter a valid amount.")
        else:
            cursor.execute("UPDATE users SET balance = balance - ? WHERE account_number = ?",
                           (amount, user[5]))
            conn.commit()
            print(f"Successfully withdrew Rs. {amount:.2f}.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# View balance
def view_balance(user):
    try:
        conn = sqlite3.connect('banking_system.db')
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM users WHERE account_number = ?", (user[5],))
        balance = cursor.fetchone()[0]
        print(f"Your current balance is: Rs. {balance:.2f}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Main function
def main():
    init_db()
    while True:
        print("\nSTATE BANK OF INDIA")
        print("1. Register as a new user")
        print("2. Login as an existing user")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_new_user()
        elif choice == '2':
            authenticate_user()
        elif choice == '3':
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
