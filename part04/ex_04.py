"""
A function named square_of_hashes, which draws a square of hash characters. 
The function takes one argument, which determines the length of the side of the square.
The function should call the function line from the exercise prior for the actual printing out. 
Copy your solution to that exercise prior the code for this exercise. Please don't change anything in the line function.
"""

def line(length, text):
    if text == "":
        character = "*"
    else:
        character = text[0]
    
    print(f"{character * length}")

def square_of_hashes(size):
    length = size
    while length > 0:
        line(size, "#")
        length -= 1
