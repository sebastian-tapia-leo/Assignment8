#import from other file
from BankAccount import BankAccount

# action to deposit money
def make_deposit(account):
    try:
        amount = float(input("How much would you like to deposit?\n"))
        account.deposit(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")

# make a withdrawal 
def make_withdrawal(account):
    try:
        amount = float(input("How much would you like to withdraw?\n"))
        account.withdraw(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")

#see account balance
def view_account(account):
    account.display_info()


def main():
    print("Welcome to the Bank!")

    name = input("Please enter your name:\n")
    account = BankAccount(name)

    while True:
        print("\nPlease choose an option:")
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. View account information")
        print("4. Quit")

        choice = input()

        if choice == "1":
            make_deposit(account)

        elif choice == "2":
            make_withdrawal(account)

        elif choice == "3":
            view_account(account)

        elif choice == "4":
            print("Thank you for your business!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
