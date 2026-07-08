"""
Implement other methods to the LunchCard and PaymentTerminal class.
"""

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        lunch_price = 2.50
        if payment >= lunch_price:
            self.funds += lunch_price
            self.lunches += 1
            return payment - lunch_price  # Return the change
        else:
            return payment  

    def eat_special(self, payment: float):
        special_price = 4.30
        if payment >= special_price:
            self.specials += 1
            return payment - special_price  # Return the change
        
        else:
            return payment  

    def eat_lunch_lunchcard(self, card: LunchCard):
        lunch_price = 2.50
        sucess = card.subtract_from_balance(lunch_price)
        if sucess:
            self.lunches += 1
        return sucess


    def eat_special_lunchcard(self, card: LunchCard):
        special_price = 4.30
        sucess = card.subtract_from_balance(special_price)
        if sucess:
            self.specials += 1
        return sucess


    def deposit_money_on_card(self, card: LunchCard, amount: float):
        if amount > 0:
            card.deposit_money(amount)
            self.funds += amount
        pass
