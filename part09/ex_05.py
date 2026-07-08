"""
Adding methods to compare properties in a class (RealProperty).
"""

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to):
        if self.square_metres > compared_to.square_metres:
            return True
        else:
            return False

    def price_difference(self, compared_to):
        price_self = self.square_metres * self.price_per_sqm
        price_compared = compared_to.square_metres * compared_to.price_per_sqm
        return abs(price_self - price_compared)

    def more_expensive(self, compared_to):
        price_self = self.square_metres * self.price_per_sqm
        price_compared = compared_to.square_metres * compared_to.price_per_sqm
        if price_self > price_compared:
            return True
        else:
            return False
