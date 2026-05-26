"""
A program which asks the user to type in a string then prints out all the substrings which begin with the first character, from the shortest to the longest.
"""

word = input("Please type in a string: ")
length = len(word)
limit = 1

while limit <= length:
    print(word[0:limit])
    limit += 1
