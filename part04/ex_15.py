"""
A program which asks the user for words. 
If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.
"""

words = []

while True:
    word_input = input("Word: ")

    if word_input in words:
        print(f"You typed in {len(words)} different words")
        break
    words.append(word_input)
