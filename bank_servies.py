from db.database import get_db_connection

def perform_operations(user):
    """
    Display available banking operations and execute user's choice.
    """
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

def deposit(user):
    """
    Deposit money into the user's account.
    """
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Invalid amount. Deposit amount must be greater than zero.")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET balance = balance + ? WHERE account_number = ?",
                       (amount, user[5]))
        conn.commit()
        conn.close()

        print(f"Successfully deposited Rs. {amount:.2f}.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def withdraw(user):
    """
    Withdraw money from the user's account.
    """
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount. Withdrawal amount must be greater than zero.")
            return

        conn = get_db_connection()
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
        conn.close()
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

def view_balance(user):
    """
    Display the user's current balance.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE account_number = ?", (user[5],))
    balance = cursor.fetchone()[0]
    conn.close()

    print(f"Your current balance is: Rs. {balance:.2f}")
