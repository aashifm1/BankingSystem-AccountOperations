import sys
import os

# Ensure the project root is in the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from db.database import init_db
from services.user_service import register_new_user, authenticate_user

print("\nWELCOME TO THE STATE BANK OF INDIA")

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
