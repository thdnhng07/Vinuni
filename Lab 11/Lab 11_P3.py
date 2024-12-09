class BankAccount:
    """
    A class to represent a bank account with balance and interest rate.

    Attributes:
        balance (float): The current balance in the bank account.
        interest_rate (float): The interest rate applied to the account balance.
    """

    def __init__(self, balance, interest_rate):
        """
        Initializes the BankAccount with a starting balance and an interest rate.

        Args:
            balance (float): The initial balance of the account.
            interest_rate (float): The interest rate for the account.
        """
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        """
        Adds a specified amount to the account balance.

        Args:
            amount (float): The amount to be deposited into the account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal is successful, False if there are insufficient funds.
        """
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        """
        Retrieves the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self.balance

    def apply_interest(self, interest_rate):
        """
        Applies the interest rate to the current balance.

        Args:
            interest_rate (float): The interest rate to be applied.
        """
        self.balance = self.balance * interest_rate

    def __str__(self):
        """
        Returns a string representation of the account with the current balance.

        Returns:
            str: A formatted string showing the current balance.
        """
        return f'Current balance: {self.balance:.1f}'


# Input handling
# Parse inputs: balance, interest rate, deposit amount, and withdrawal amount
balance, interest_rate, deposit, withdrawal = map(lambda x: float(x) if '.' in x else int(x), input().split())

# Create a BankAccount instance
account = BankAccount(balance, interest_rate)

# Deposit the specified amount and print the account details
account.deposit(deposit)
print(account)

# Attempt to withdraw the specified amount and print the result
if account.withdraw(withdrawal):
    print(account)
else:
    print(False)

# Apply the interest rate and print the updated account details
account.apply_interest(interest_rate)
print(account)
