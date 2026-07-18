"""
A function named lengths(lists: list) which takes a list containing lists of integers as its argument and return a new list, containing the lengths of the lists within the argument list.
"""

def lengths(lists: list) -> list:
    return [len(list) for list in lists]
