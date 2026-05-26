"""
A program that prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. 
You may assume the input string is at least three characters long.
"""

word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = 0

while index <= len(word) -3:
    if word[index] == character:
        print(word[index:index+3])
    index += 1
