"""
A program which asks for the user's age.
If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.
"""

age = int(input("What is your age? "))
if age < 0:
    print("That must be a mistake")
elif age < 5:
    print("I suspect you can't write quite yet...")
else:
    print("Ok, you're " + str(age) + " years old")
