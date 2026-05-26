"""
A program which asks the user for a string and an amount then prints out the string as many times as specified by the amount. The printout should all be on one line, with no extra spaces or symbols added.
"""

string = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))
print(f"{string*amount}")
