#5  |   Create a bank account class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Invalid input:: amount must be posititve")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Available balance: {self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Invalid input:: Withdrawal amount must be positive.")


account = Account("Nurasyl", 100)
account.deposit(200)
account .withdraw(300)