"""
A recursive function named recursive_sum(number: int) which calculates the sum 1 + 2 + ... + number.
"""

def recursive_sum(number: int):
    if number <= 1:
        return number
    return number + recursive_sum(number -1)
