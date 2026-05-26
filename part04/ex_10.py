"""
A function named same_chars, which takes one string and two integers as arguments. 
The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. 
Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.
"""

def same_chars(word, index1, index2):
    if 0 <= index1 < len(word) and 0 <= index2 < len(word):
        return word[index1] == word[index2]
    return False
