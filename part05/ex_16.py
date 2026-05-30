"""
A function named histogram, which takes a string as its argument. 
The function should print out a histogram representing the number of times each letter occurs in the string. 
Each occurrence of a letter should be represented by a star on the specific line for that letter.
"""

def histogram (text: str):
    char_list = []
    for char in text:
        if char not in char_list:
            char_list.append(char)
            print(f"{char} " + '*' * text.count(char))
