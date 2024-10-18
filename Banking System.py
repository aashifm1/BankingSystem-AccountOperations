import random
import getpass

print("\nSTATE BANK OF OCEAN")

users_db = {
    "user123": "password123"
}

def user_type():
    user_type = input("Enter user type (new,existing): ").lower()
    if user_type == "new":
        print("\nYou are a new user. Welcome Sir/Madam")
        newperson()
    elif user_type == "existing":
        print("\nYou are an existing user. Welcome Sir/Madam")
        authenticate_user()
    else:
        print("Invalid user type. Please enter a valid user type.")

def newperson():
    def validate():
        while True:
            try:
                age = int(input("Enter your age: "))
                if age >= 18:
                    print("You are eligible to open an account in the bank.")
                    eligible()
                    break
                else:
                    print("Not eligible. Only people over 18 can have an account.")
            except ValueError:
                print("Invalid input. Please enter a valid age.")

    def eligible():
        name = input("\nName: ")
        dob = input("Date of Birth (DD/MM/YYYY): ")
        acc_type = input("Account type (Personal/Business): ").lower()
        if acc_type == "personal":
            print("Maximum withdrawal limit for Personal account is Rs. 40,000")
        elif acc_type == "business":
            print("Maximum withdrawal limit for Business account is Rs. 1,00,000")
        else:
            print("Invalid account type.")
            return

        def gen_acc_no(base_number="314151000", random_length=5):
            random_part = ''.join([str(random.randint(0, 9)) for _ in range(random_length)])
            acc_no = base_number + random_part
            return acc_no

        new_acc_no = gen_acc_no()
        print("New Generated account number:", new_acc_no)

    validate()

def authenticate_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")  # Hides password input
    if username in users_db and users_db[username] == password:
        print("Login successful. Welcome back!")
        oldperson()
    else:
        print("Invalid username or password. Access denied.")

def oldperson():
    print("Welcome back!")
    operation()

def operation():
    oper = input("What are you going to do (Cash Deposit/Cash Withdrawal): ").lower()
    if oper == "cash deposit":
        print("\nCash deposit process started...")
        deposit()
    elif oper == "cash withdrawal":
        print("\nCash withdrawal process started...")
        withdrawal()
    else:
        print("\nInvalid Operation")

def deposit():
    while True:
        try:
            deposit_type = int(input("Deposit type (1-Deposit amount/2-Transfer amount): "))
            if deposit_type == 1:
                money_in = float(input("Cash Deposit Amount: "))
                acc_no = input("Account Number: ")
                if len(acc_no) != 14 or not acc_no.isdigit():
                    print("Invalid account number. Please enter a 14-digit account number.")
                    continue
                print(f"Processing deposit of Rs. {money_in:.2f} to account no ending with {acc_no[-4:]}.")
                break
            elif deposit_type == 2:
                from_acc_no = input("Your Account Number: ")
                to_acc_no = input("Transfer Account Number: ")
                money_in_from = float(input("Transfer Amount: "))
                if len(from_acc_no) != 14 or not from_acc_no.isdigit() or len(to_acc_no) != 14 or not to_acc_no.isdigit():
                    print("Invalid account number. Please enter a 14-digit account number.")
                    continue
                print(f"Processing transfer of Rs. {money_in_from:.2f} from account no ending with {from_acc_no[-4:]} to account no ending with {to_acc_no[-4:]}.")
                break
            else:
                print("Invalid deposit type. Select 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def withdrawal():
    while True:
        try:
            money_out = float(input("Cash Withdrawal Amount: "))
            acc_no = input("Account Number: ")
            if len(acc_no) != 14 or not acc_no.isdigit():
                print("Invalid account number. Please enter a 14-digit account number.")
                continue
            print(f"Processing withdrawal of Rs. {money_out:.2f} from account no ending with {acc_no[-4:]}.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

user_type()
