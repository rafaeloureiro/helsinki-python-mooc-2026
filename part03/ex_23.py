"""
A program which asks the user for a positive integer number then prints out a list of multiplication operations until both operands reach the number given by the user.
"""

number = int(input("Please type in a number: "))
counter1 = 1
while counter1 <= number:
    counter2 = 1
    while counter2 <= number:
        print(f"{counter1} x {counter2} = {counter1*counter2}")
        counter2 += 1
    counter1 += 1
