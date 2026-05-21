"""
A program which asks the user for an integer number and then print out the magnitude of the number according to certain limits.
"""

number = int(input("Please type in a number:"))
if number < 1000:
    print(f"This number is smaller than 1000")
if number < 100:
    print(f"This number is smaller than 100")
if number < 10:
    print(f"This number is smaller than 10")
print(f"Thank you!")
