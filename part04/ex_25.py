"""
A function named sum_of_positives, which takes a list of integers as its argument. 
The function returns the sum of the positive values in the list.
"""

def sum_of_positives(numbers : list[int]):
    soma = 0
    for num in numbers:
        if num > 0:
            soma += num
    return soma
