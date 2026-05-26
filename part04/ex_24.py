"""
A function named palindromes, which takes a string argument and returns True if the string is a palindrome. 
Palindromes are words which are spelled exactly the same backwards and forwards.
"""

def palindromes(word: str):
    return word == word[::-1]


while True:
    guess = input("Please type in a palindrome: ")
    
    if palindromes(guess):
        print(f"{guess} is a palindrome!")
        break 
    else:
        print("that wasn't a palindrome")
