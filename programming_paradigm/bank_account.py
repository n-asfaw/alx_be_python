class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Private attribute for account balance

    def deposit(self, amount):
        if amount > 0:  # Ensure that the deposit amount is positive
            self._account_balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:  # Check for sufficient funds
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

