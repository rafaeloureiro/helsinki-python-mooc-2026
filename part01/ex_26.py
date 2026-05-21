"""
A program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. 
If the user types in anything else, the program should print out nothing.
"""

number01 = int(input("Number 1:"))
number02 = int(input("Number 2:"))
operation = input("Please type a operation:")
if operation == "add":
    print(f"{number01} + {number02} = {number01+number02}")
if operation == "subtract":
    print(f"{number01} - {number02} = {number01-number02}")
if operation == "multiply":
    print(f"{number01} * {number02} = {number01*number02}")
