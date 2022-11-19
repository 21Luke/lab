class Account:

    def __init__(self, name: str) -> None:
        """
        this function is used to create the variable account_name and account_balance
        :param name: name of the account
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        this function is used to deposit money into account_balance
        :param amount: the amount of money the user wishes to deposit into account_balance
        :return: It will return True if successful and return False if it fails
        """
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        elif amount < 0:
            return False
        elif amount == 0:
            return False

    def withdraw(self, amount: float) -> bool:
        """
            this function is used to withdraw money from account_balance
            :param amount: the amount of money the user wishes to withdraw
            :return: It will return True if successful and return False if it fails
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance = self.__account_balance - amount
            return True
        elif amount == 0:
            return False
        elif amount > self.__account_balance:
            return False
        elif amount < 0:
            return False

    def get_balance(self)-> float:
        """
            this function is used to get the final balance
            :return: it returns the account_balance
        """
        return self.__account_balance

    def get_name(self)-> str:
        """
        This function is used to get the name of the account

        :return: it returns the account_name
        """
        return self.__account_name