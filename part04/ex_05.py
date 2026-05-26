"""
A function named square, which prints out a square of characters, and takes two arguments. 
The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square.
The function should call the function line from the exercise prior for the actual printing out. 
Copy your solution to that exercise prior the code for this exercise. Please don't change anything in the line function.
"""

def line(length, text):
    
    if text == "":
        character = "*"
    else:
        character = text[0]
    print(f"{character * length}")

def square(size, character):
    
    rows = size
    while rows > 0:
        line(size, character)
        rows -= 1       
