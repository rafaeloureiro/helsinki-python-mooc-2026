"""
A function that creates a new dictionary that it's values are the original dictionary times 10
"""

def times_ten(start_index: int, end_index: int):
    numbers = {}
    for i in range(start_index, end_index + 1):
        numbers[i] = i * 10
    return numbers
