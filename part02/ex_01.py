"""
A print with many conditional statements.
"""

number = int(input("Please type in a number: "))
if number>100:
    print(f"The number was greater than one hundred")
    number = number - 100
    print(f"Now its value has decreased by one hundred")
    print(f"Its value is now {number}")
print(f"{number} must be my lucky number!")
print(f"Have a nice day!")
