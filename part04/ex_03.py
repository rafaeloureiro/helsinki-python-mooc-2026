"""
A function named box_of_hashes, which prints out a rectangle of hash characters. 
The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

The function should call the function line from the exercise prior for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything in your line function.
"""

def line(length, text):
    if text == "":
        character = "*"
    else:
        character = text[0]
    
    print(f"{character * length}")

def box_of_hashes(height):
    while height >  0:
        line(10, "#")
        height -= 1
