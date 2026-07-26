"""
A class named LotteryNumbers which takes the week number (an integer value) and a list of seven integers as its constructor arguments. 
The list contains the correct lottery numbers for the given week.
A method named number_of_hits(numbers: list) which takes a list of integers as its argument. 
The method returns the number of correct entries in the parameter list.
"""

class LotteryNumbers:
    def __init__(self, week: int, numbers: list):
        self.week = week
        self.numbers = numbers

    def number_of_hits(self, numbers: list) -> int:
        return len([number for number in numbers if number in self.numbers])

    def hits_in_place(self, numbers: list) -> list:
        return [number if number in self.numbers else -1 for number in numbers]
