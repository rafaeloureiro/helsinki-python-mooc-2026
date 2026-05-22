"""
A program that compares two words and print out the word that comes alphabetically last.
"""

word01= input("Please type in the 1st word: ").lower()
word02= input("Please type in the 2nd word: ").lower()
if word01 == word02:
    print("You gave the same word twice.")
elif word01 > word02:
    print(f"{word01} comes alphabetically last.")
elif word02 > word01:
    print(f"{word02} comes alphabetically last.")
