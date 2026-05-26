"""
A program which asks the user to type in a string then prints out all the substrings which end with the last character, from the shortest to the longest. 
"""

string = input("Please type in a string: ")
 
start = len(string) - 1
while start >= 0:
    print(string[start:])
    start -= 1
