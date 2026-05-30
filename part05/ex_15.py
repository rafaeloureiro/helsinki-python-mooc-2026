"""
A function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary.
"""

def factorials(end_index: int, start_index: int = 1) -> dict:
    result = {}
    for i in range(start_index, end_index + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        result[i] = factorial
    return result
