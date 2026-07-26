"""
A function named remove_smaller_than(numbers: list, limit: int) which takes a list of integers and a limit value (also in integer format) as its arguments.
The function use a list comprehension to produce a new list without the values which are smaller than the limit value.
"""

def remove_smaller_than(numbers: list, limit: int) -> list:
    return [number for number in numbers  if number >= limit]
