"""
Class defines a an account class
"""

from colorama import Fore, Style


class Account:
    """
    Account class
    """

    def __init__(self, name: str, balance: float, password: str) -> None:
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount_to_deposit: float, password: str) -> float | None:
        """Deposits money into the account

        Args:
            amount_to_deposit (float): The amount of money to deposit
            password (str): The password of the account

        Returns:
            _type_: None
        """
        if password != self.password:
            print(f"{Fore.RED}Invalid Password{Style.RESET_ALL}")
            return None

        if amount_to_deposit <= 0:
            print(f"{Fore.RED}Invalid Amount{Style.RESET_ALL}")
            return None

        self.balance += amount_to_deposit
        return self.balance

    def withdraw(
        self, amount_to_withdraw: float, password: str
    ) -> float | None:
        """Withdraws money from the account

        Args:
            amount_to_withdraw (float): The amount of money to dispense
            password (str): The password of the account
        """
        if password != self.password:
            print(f"{Fore.RED}Invalid Password{Style.RESET_ALL}")
            return None

        if amount_to_withdraw <= 0:
            print(f"{Fore.RED}Invalid Amount{Style.RESET_ALL}")
            return None

        if amount_to_withdraw > self.balance:
            print(f"{Fore.RED}Insufficient Funds{Style.RESET_ALL}")
            return None

        self.balance -= amount_to_withdraw
        return self.balance

    def get_balance(self, password: str) -> float | None:
        """Returns the balance of the account

        Args:
            password (str): The password of the account

        Returns:
            float: The balance of the account
        """

        if password != self.password:
            print(f"{Fore.RED}Invalid Password{Style.RESET_ALL}")
            return None

        return self.balance
