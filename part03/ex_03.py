"""
A program which asks the user for a number then prints out all integer numbers greater than zero but smaller than the input in ascending order.
Each number is printed in differente lines.
"""

limit = int(input("Upper limit: "))
number = 1
while number < limit:
    print(number)
    number += 1
