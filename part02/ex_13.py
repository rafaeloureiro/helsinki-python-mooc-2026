"""
A program which asks the user for three letters and then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
"""

letter01 = input("1st letter: ")
letter02 = input("2nd letter: ")
letter03 = input("3rd letter: ")

letters = sorted([letter01, letter02, letter03], key=str.lower)

print(f"The letter in the middle is {letters[1]}")
