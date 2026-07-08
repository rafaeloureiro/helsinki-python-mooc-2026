"""
A class with encapsulated attributes and a getter method, alongside other methods, within a single class
"""

class BankAccount:
    def __init__(self, __owner: str, __account_number: str, __balance: float):
        self.__owner = __owner
        self.__account_number = __account_number
        self.__balance = __balance

    def deposit(self, __amount: float):
        if __amount > 0:
            self.__balance += __amount
            self.__service_charge()
        else:
            raise ValueError("Deposit amount must be positive.")
        
    def withdraw(self, __amount: float):
        if __amount > 0:
            if __amount <= self.__balance:
                self.__balance -= __amount
                self.__service_charge()
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Withdrawal amount must be positive.")
        
    @property    
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        self.__balance = self.__balance * (0.99)
