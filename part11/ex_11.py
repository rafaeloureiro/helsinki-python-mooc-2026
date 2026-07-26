"""
A function named lengths(strings: list) which takes a list of strings as its argument. 
The function returns a dictionary with the strings in the list as the keys and their lengths as the values.
The function is implemented with a dictionary comprehension.
"""

def lengths(strings: list) -> dict:
    return {string: len(string) for string in strings}
