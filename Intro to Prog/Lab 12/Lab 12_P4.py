class Account:
    """
    Base class representing a bank account.

    Attributes:
        __account_id (int): Unique identifier for the account
        __balance (float): Current balance of the account

    Methods:
        deposit(amount: float) -> str: Deposits money into the account
        withdraw(amount: float) -> str: Withdraws money from the account
        get_balance() -> float: Returns the current balance
        get_account_id() -> int: Returns the account ID
    """

    def __init__(self, account_id: int, balance: float = 0):
        """
        Initializes an Account object.

        Args:
            account_id (int): Unique identifier for the account
            balance (float, optional): Initial balance. Defaults to 0.
        """
        self.__account_id = account_id
        self.__balance = balance

    def deposit(self, amount: float) -> str:
        """
        Deposits money into the account.

        Args:
            amount (float): Amount to deposit

        Returns:
            str: Message indicating success or failure
        """
        if amount <= 0:
            return "Invalid deposit amount."
        self.__balance += amount
        return f"Deposit successful to account {self.__account_id}. Updated balance: {int(self.__balance)}"

    def withdraw(self, amount: float) -> str:
        """
        Withdraws money from the account.

        Args:
            amount (float): Amount to withdraw

        Returns:
            str: Message indicating success or failure
        """
        if amount <= 0:
            return "Invalid withdrawal amount."
        if amount > self.__balance:
            return "Insufficient balance."
        self.__balance -= amount
        return f"Withdrawal successful from account {self.__account_id}. Updated balance: {self.__balance}"

    def get_balance(self) -> float:
        """
        Returns the current account balance.

        Returns:
            float: Current balance
        """
        return self.__balance

    def get_account_id(self) -> int:
        """
        Returns the account ID.

        Returns:
            int: Account ID
        """
        return self.__account_id


class CheckingAccount(Account):
    """
    Subclass of Account representing a checking account with fees.

    Attributes:
        __fee (float): Fee charged on withdrawals

    Methods:
        get_fee() -> float: Returns the fee amount
        set_fee(new_fee: float) -> None: Sets the fee amount
    """

    def __init__(self, account_id: int, balance: float = 0, fee: float = 5):
        """
        Initializes a CheckingAccount object.

        Args:
            account_id (int): Unique identifier for the account
            balance (float, optional): Initial balance. Defaults to 0.
            fee (float, optional): Initial fee amount. Defaults to 5.
        """
        super().__init__(account_id, balance)
        self.__fee = fee

    def withdraw(self, amount: float) -> str:
        """
        Withdraws money from the checking account, including the fee.

        Args:
            amount (float): Amount to withdraw

        Returns:
            str: Message indicating success or failure
        """
        if amount <= 0:
            return "Invalid withdrawal amount."
        total_amount = amount + self.__fee
        if total_amount > self.get_balance():
            return "Insufficient balance."
        self._Account__balance -= total_amount  
        return f"Withdrawal successful from account {self.get_account_id()} (including fee of {self.__fee}). Updated balance: {int(self.get_balance())}"

    def get_fee(self) -> float:
        """
        Returns the current fee amount.

        Returns:
            float: Fee amount
        """
        return self.__fee

    def set_fee(self, new_fee: float) -> None:
        """
        Sets the fee amount for the checking account.

        Args:
            new_fee (float): New fee amount to set
        """
        self.__fee = new_fee


# Main program logic
n = int(input())
accounts = {}

for i in range(n):
    command = input().split()
    account_id = int(command[0])
    
    if len(command) == 2: 
        balance = float(command[1])
        if account_id not in accounts:
            accounts[account_id] = CheckingAccount(account_id, balance)
            print(f"Account {account_id} created with balance: {int(balance)}")
        else:
            print(f"Account already exists.")
    elif len(command) == 3: 
        action = command[1]
        if account_id not in accounts:
            print(f"Account does not exist.")
        else:
            account = accounts[account_id]
            amount = float(command[2])
            if action == "deposit":
                print(account.deposit(amount))
            elif action == "withdraw":
                print(account.withdraw(amount))
            else:
                print(f"Invalid action: {action}.")
    else:
        print("Invalid command format.")