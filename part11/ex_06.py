"""
A function named begin_with_vowel(words: list) which takes a list of strings as its argument.
The function use a list comprehension technique to create and return a new list, containing only those words from the original list which begin with a vowel (a, e, i, o, u). 
Both lowercase and uppercase letters should be accepted.
"""

def begin_with_vowel(words: list) -> list:
    return [word for word in words if word[0].lower() in "aeiou"]
