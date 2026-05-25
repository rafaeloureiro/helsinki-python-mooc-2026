"""
A program which asks the user to type in a limit. 
The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user.
The program should print the sum of the consecutive numbers and also the calculation performed.
Assume the number typed in by the user is always equal to 2 or higher
"""

limit = int(input("Limit: "))
number = 1
total_sum = 1
calculation = "1"

while total_sum < limit:
    number += 1
    total_sum += number
    calculation += f" + {number}"
print(f"The consecutive sum: {calculation} = {total_sum}")
