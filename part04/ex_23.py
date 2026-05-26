"""
A function named anagrams, which takes two strings as arguments. 
The function returns True if the strings are anagrams of each other. 
Two words are anagrams if they contain exactly the same characters.
"""

def anagrams(word1,word2):
    if sorted(word1) == sorted(word2):
        return True
    else:        
        return False   
