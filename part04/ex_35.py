"""
A function named no_vowels, which takes a string argument. 
The function returns a new string, which should be the same as the original but with all vowels removed.
"""

def no_vowels(my_string: str):
    vowels = "aeiou"
    result = ""
 
    for letter in my_string:
        if letter not in vowels:
            result += letter
 
    return result
