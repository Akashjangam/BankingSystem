import os
import datetime

# File Handling in Python
ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

# Function to create an account
def create_account():
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit: "))
    account_number = str(abs(hash(name + str(datetime.datetime.now()))) % 1000000)  # Generate a 6-digit account number
    password = input("Enter a password: ").strip()
    
    with open(ACCOUNTS_FILE, "a") as f:
        f.write(f"{account_number},{name},{password},{initial_deposit}\n")
    
    print(f"Account created successfully! Your account number is {account_number}")

# Function to log transactions
def log_transaction(account_number, transaction_type, amount):
    with open(TRANSACTIONS_FILE, "a") as f:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        f.write(f"{account_number},{transaction_type},{amount},{date}\n")

# Function to authenticate user
def authenticate():
    account_number = input("Enter your account number: ").strip()
    password = input("Enter your password: ").strip()
    
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as f:
            for line in f:
                acc_no, name, stored_password, balance = line.strip().split(",")
                if acc_no == account_number and stored_password == password:
                    print("Login successful!")
                    return acc_no, name, float(balance)
    print("Invalid credentials! Please try again.")
    return None, None, None

# Function to update account balance
def update_balance(account_number, new_balance):
    lines = []
    with open(ACCOUNTS_FILE, "r") as f:
        for line in f:
            acc_no, name, password, balance = line.strip().split(",")
            if acc_no == account_number:
                lines.append(f"{acc_no},{name},{password},{new_balance}\n")
            else:
                lines.append(line)
    
    with open(ACCOUNTS_FILE, "w") as f:
        f.writelines(lines)

# Primitive and Abstract Data Structures
# Function to perform deposit or withdrawal
def perform_transaction():
    account_number, name, balance = authenticate()
    if account_number:
        print(f"Welcome, {name}! Your current balance is: {balance}")
        print("1. Deposit")
        print("2. Withdraw")
        choice = input("Enter your choice: ").strip()
        amount = float(input("Enter amount: ").strip())
        
        if choice == "1":
            balance += amount
            log_transaction(account_number, "Deposit", amount)
            print(f"Deposit successful! New balance: {balance}")
        elif choice == "2":
            if amount > balance:
                print("Insufficient balance!")
                return
            balance -= amount
            log_transaction(account_number, "Withdrawal", amount)
            print(f"Withdrawal successful! New balance: {balance}")
        else:
            print("Invalid choice!")
            return
        
        update_balance(account_number, balance)

# Conditional Statements, Loops, and Input Handling in Python
# Main menu
def main():
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Login and Perform Transactions")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            perform_transaction()
        elif choice == "3":
            print("Thank you for using our Banking System!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
# git remote set-url origin https://GitHub_pat_11BMCDHZY0h7HWuDzdGdWN_8Fir8zOHKoiqEoBPL99WJYCCguhrT7EIzdDlfVC1vypRCNL5BIAtCuUvg8l@github.com/Akashjangam