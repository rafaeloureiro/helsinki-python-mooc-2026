"""
A function named lottery_numbers(amount: int, lower: int, upper: int), which generates as many random numbers as specified by the first argument. 
All numbers should fall within the bounds lower to upper. The numbers should be stored in a list and returned. 
The numbers should be in ascending order in the returned list.
"""

from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers_range = list(range(lower, upper + 1))
    return sorted(sample(numbers_range, amount))
