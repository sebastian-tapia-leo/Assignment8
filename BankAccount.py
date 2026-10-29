# Sebastian Tapia
# IS 303 Assignment 8 Bank Account
import random

# Make class/entity for bank account and define actions within class
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: ${self.balance:.2f}")
        else:
            print("Please enter a positive amount.")

    # use if loop to create withdraw action
    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a positive amount.")
        elif amount > self.balance:
            print("Insufficient funds. You cannot withdraw that much.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance:.2f}")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
