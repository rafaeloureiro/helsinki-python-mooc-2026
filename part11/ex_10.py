"""
A function named cheaper_properties(properties: list, reference: RealProperty) which takes a list of properties and a single RealProperty object as its arguments. 
The function returns a list containing only those properties in the original list which are cheaper than the reference property, along with the price difference. 
The items in the returned list are a tuples, where the first item is the property itself and the second is the difference in price.
"""

class RealProperty:
    def __init__(self, rooms: int , square_meters: int, price_per_sqm: int, description: str):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
        self.description = description
        self.properties = []

    def bigger(self, compared_to):
        return self.square_meters > compared_to.square_meters

    def price_difference(self, compared_to):
        # Function abs returns absolute value
        difference = abs((self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters))
        return difference

    def more_expensive(self, compared_to):
        difference = (self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters)
        return difference > 0


    def __repr__(self):
        return (f'RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, ' + 
            f'price_per_sqm = {self.price_per_sqm}, description = {self.description})')
    
def cheaper_properties(properties: list, reference: RealProperty) -> list:
    return [(property, property.price_difference(reference)) for property in properties if reference.more_expensive(property)]
