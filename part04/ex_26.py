"""
A function named even_numbers, which takes a list of integers as an argument. 
The function returns a new list containing the even numbers from the original list.
"""

def even_numbers(numbers : list[int]):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum
