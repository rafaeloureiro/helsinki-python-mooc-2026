"""
A function named most_common_character, which takes a string argument. 
The function returns the character which has the most occurrences within the string. 
If there are many characters with equally many occurrences, the one which appears first in the string should be returned.
"""

def most_common_character(string):
    character_count = {}
    
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
            
    most_common_char = max(character_count, key=character_count.get)
    
    return most_common_char
