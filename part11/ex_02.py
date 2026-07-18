"""
A function named rows_of_stars(numbers: list) which takes a list of integers as its argument and return a new list containing rows of stars.
"""

def rows_of_stars(numbers: list) -> list:
    return ['*' * number for number in numbers]
