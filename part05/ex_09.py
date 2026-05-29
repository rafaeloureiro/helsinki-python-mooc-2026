"""
A functions that find and remove the smallest item in the list.
"""

def remove_smallest(numbers: list):
    smallest = min(numbers)
    numbers.remove(smallest)
