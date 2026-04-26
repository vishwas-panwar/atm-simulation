balance = 1000
transactions = []

# Function to display balance
def display_balance():
    print("Your balance is: ₹", balance)

# Function to deposit money
def deposit_money():
    global balance
    amount = float(input("Enter amount to deposit: "))
    
    if amount > 0:
        balance = balance + amount
        transactions.append("Deposited ₹" + str(amount))
        print("Money deposited successfully")
    else:
        print("Invalid amount")

# Function to withdraw money
def withdraw_money():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance = balance - amount
        transactions.append("Withdrawn ₹" + str(amount))
        print("Money withdrawn successfully")

# Function to show statement
def show_statement():
    print("\n--- Transaction Statement ---")
    
    if len(transactions) == 0:
        print("No transactions yet")
    else:
        for t in transactions:
            print(t)

# Main ATM function
def atm():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_balance()

        elif choice == "2":
            deposit_money()

        elif choice == "3":
            withdraw_money()

        elif choice == "4":
            show_statement()

        elif choice == "5":
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice, try again")

# Run program
atm()