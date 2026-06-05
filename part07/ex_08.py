"""
A function named words(n: int, beginning: str), which returns a list containing n random words from the words.txt file. 
All words should begin with the string specified by the second argument.
"""

from random import sample

def words(n: int, beginning: str) -> list:
    with open("words.txt") as doc:
        word_list = [word.strip() for word in doc if word.strip().startswith(beginning)]

    if len(word_list) < n:
        raise ValueError(f"Not enough words starting with '{beginning}'")

    return sample(word_list, n)
