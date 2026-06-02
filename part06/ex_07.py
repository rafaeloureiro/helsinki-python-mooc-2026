"""
A program which asks the user to type in some text. 
Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them.
"""

word_list = set()
with open("wordlist.txt") as file:
    for line in file:
        word_list.add(line.strip())

user_text = input("Write text: ")
check = user_text.split()

result = []
for word in check:
    if word.lower() not in word_list:
        result.append(f"*{word}*")
    else:
        result.append(word)

print(" ".join(result))
