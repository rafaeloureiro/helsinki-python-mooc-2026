"""
Using len function to count characters.
"""

word = input("Please type in a word:")
count = len(word)
if count > 1:
    print(f"There are {count} letters in the word {word}")
print(f"Thank you!")
