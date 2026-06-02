"""
A program which functions as a dictionary. The user can type in new entries or look for existing entries.
"""

dictionary = {}

with open("dictionary.txt", "a"):
    pass

with open("dictionary.txt") as file:
    for line in file:
        word_finnish, word_english = line.strip().split(";")
        dictionary[word_finnish] = word_english

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    option = input("Function: ")

    if option == "1":
        word_finnish = input("The word in Finnish: ")
        word_english = input("The word in English: ")

        dictionary[word_finnish] = word_english

        with open("dictionary.txt", "a") as file:
            file.write(f"{word_finnish};{word_english}\n")

        print("Dictionary entry added")

    elif option == "2":
        search_word = input("Search term: ")

        for word_finnish, word_english in dictionary.items():
            if search_word in word_finnish or search_word in word_english:
                print(f"{word_finnish} - {word_english}")

    elif option == "3":
        print("Bye!")
        break
