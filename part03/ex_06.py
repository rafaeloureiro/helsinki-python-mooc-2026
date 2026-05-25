"""
A program which asks the user to type in a limit. 
The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user.
"""

limit = int(input("Limit: "))
number = 0
total_sum = 0 

while total_sum < limit:
    number += 1
    total_sum += number
print(total_sum)
