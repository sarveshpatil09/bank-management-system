import json

accounts = {}

def create_account():
    name = input("Enter account holder name: ")
    acc_no = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))

    accounts[acc_no] = {
        "name": name,
        "balance": balance
    }

    print("Account created successfully\n")


def deposit():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))

    if acc_no in accounts:
        accounts[acc_no]["balance"] += amount
        print("Deposit successful\n")
    else:
        print("Account not found\n")


def withdraw():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))

    if acc_no in accounts:
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful\n")
        else:
            print("Insufficient balance\n")
    else:
        print("Account not found\n")


def check_balance():
    acc_no = input("Enter account number: ")

    if acc_no in accounts:
        print("Account Holder:", accounts[acc_no]["name"])
        print("Balance:", accounts[acc_no]["balance"])
    else:
        print("Account not found\n")


def save_data():
    with open("accounts.json","w") as f:
        json.dump(accounts,f)

    print("Data saved\n")


def load_data():
    global accounts
    try:
        with open("accounts.json","r") as f:
            accounts = json.load(f)
    except:
        accounts = {}


def menu():

    load_data()

    while True:

        print("\n===== Bank Management System =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Save Data")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            check_balance()

        elif choice == "5":
            save_data()

        elif choice == "6":
            save_data()
            print("Exiting system")
            break

        else:
            print("Invalid choice")


menu()
