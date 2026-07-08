"""
Implementing encapsulated atributes within a method
"""

class Car:
    def __init__(self):
        self.__tank = 0
        self.__odometer = 0
    
    def fill_up(self):
        self.__tank = 60

    def drive(self, km: int):
        distance = min(km, self.__tank)
        self.__odometer += distance
        self.__tank -= distance

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__tank} litres"
