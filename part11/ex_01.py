"""
A function named square_roots(numbers: list) which takes a list of integers as its argument and return a new list containing the square roots of the original integers.
"""

from math import sqrt

def square_roots (numbers: list) -> list:
    return [sqrt(item) for item in numbers]
