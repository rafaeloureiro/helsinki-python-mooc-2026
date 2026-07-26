"""
A recursive function named add_numbers_to_list(numbers: list). 
The function takes a list of numbers as its argument, and adds new numbers to the list until the length of the list is divisible by five. 
Each number added to the list should be one greater than the last number in the list.
"""
def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 != 0:
        numbers.append(numbers[-1] + 1)
        add_numbers_to_list(numbers)
