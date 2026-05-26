"""
A function named distinct_numbers, which takes a list of integers as its argument. 
The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.
"""

def distinct_numbers(numbers : list[int]):
  return sorted(set(numbers))
