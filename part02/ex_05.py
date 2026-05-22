"""
A program which asks for two integer numbers and then print out whichever is greater. 
If the numbers are equal, the program should print a different message.
"""

number01 = int(input("Please type in the first number:"))
number02 = int(input("Please type in another number:"))
if number01 == number02:
    print(f"The numbers are equal!")
elif number01 > number02:
    print(f"The greater number was: {number01}")
elif number02 > number01:
    print(f"The greater number was: {number02}")
