"""
A program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. 
If the strings are of equal length, the program should print out "The strings are equally long".
"""

input_string01 = input("Please type in string 1:")
input_string02 = input("Please type in string 2:")

if len(input_string01) > len(input_string02):
    print(f"{input_string01} is longer")
if len(input_string02) > len(input_string01):
    print(f"{input_string02} is longer")
if len(input_string01) == len(input_string02):
    print(f"The strings are equally long")
