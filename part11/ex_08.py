"""
A function named filter_forbidden(string: str, forbidden: str) which takes two strings as its arguments. 
The function should return a new version of the first string. It should not contain any characters from the second string.
"""

def filter_forbidden(string: str, forbidden: str):
    characters = [character for character in string if character not in forbidden]
    return "".join(characters)
