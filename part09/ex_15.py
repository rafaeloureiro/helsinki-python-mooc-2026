"""
Putting all together.
"""

class Item:
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:

    def __init__(self, max_weight: float):
        self.__max_weight = max_weight
        self.__items = []

    def total_weight(self):
        weight = 0
        for item in self.__items:
            weight += item.weight()
        return weight

    def add_item(self, item: Item):
        if self.total_weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight (self) -> int:
        return int(self.total_weight())
    
    def heaviest_item(self):
        if not self.__items:
            return None
        return max(self.__items, key=Item.weight)

    
    def __str__(self):
        if len(self.__items) == 1:
            return f"1 item ({self.total_weight()} kg)"
        return f"{len(self.__items)} items ({self.total_weight()} kg)"
    
class CargoHold:
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight
        self.__suitcases = []

    def total_weight(self):
        weight = 0
        for suitcase in self.__suitcases:
            weight += suitcase.weight()
        return weight

    def add_suitcase(self, suitcase: Suitcase):
        if self.total_weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def print_items(self):
            for suitcase in self.__suitcases:
                suitcase.print_items()

    def __str__(self):
        space_left = self.__max_weight - self.total_weight()
        if len(self.__suitcases) == 1:
            return f"1 suitcase, space for {space_left} kg"
        return f"{len(self.__suitcases)} suitcases, space for {space_left} kg"
