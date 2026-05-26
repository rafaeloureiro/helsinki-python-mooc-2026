"""
A program which asks the user which editor they are using. 
The program should keep on asking until the user types in Visual Studio Code.
"""

while True:
    editor = input("Editor: ").lower()

    if editor == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")
