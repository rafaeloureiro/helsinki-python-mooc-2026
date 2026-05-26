"""
A program which asks the user for a string then prints out the input string in reversed order, from end to beginning. 
Each character should be on a separate line.
"""

word = input("Please type in a string: ")
index = len(word) - 1

while index >= 0:
    print(word[index])
    index -= 1
