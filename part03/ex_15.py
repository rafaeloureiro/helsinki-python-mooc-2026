"""
A program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. 
If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.
Assume the input string is at most 20 characters long.
"""

word = str(input("Please type in a string: "))

if len(word) == 20:
  print(word)
else:
  print(f"{(20 - len(word)) * '*'}{word}")
