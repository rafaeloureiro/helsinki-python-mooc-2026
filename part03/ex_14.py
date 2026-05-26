"""
A program which asks the user for strings using a loop.
The program prints out each string underlined
The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.
"""

while True:
    text = input("Please type in a string: ")

    if text == "":
        break

    print(text)
    print("-" * len(text))
