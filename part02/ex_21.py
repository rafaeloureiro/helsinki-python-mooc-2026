"""
A program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.
the loop ends also if the user types in the same word twice in a row.
"""

word = input("Please type in a word: ")
search = ""
last_word = ""

while True:
  if word == "end":
    break
  elif word == last_word:
    break
  else:
    search += word + " "
    last_word = word
    word = str(input("Please type in a word: ")) 

print(f"{search}")
