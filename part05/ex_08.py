"""
A function named double_items(numbers: list), which takes a list of integers as its argument.

The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.
"""

def double_items(numbers: list):
    numbers_doubled = []
    for number in numbers:
        numbers_doubled.append(number * 2)
    return numbers_doubled
