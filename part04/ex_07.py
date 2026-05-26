"""
A function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. 
The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. 
The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.
The function should call the function line from the exercise prior for the actual printing out. 
Copy your solution to that exercise prior the code for this exercise. Please don't change anything in the line function.
"""

def line(length, text):
    if text == "":
        character = "*"
    else:
        character = text[0]
    print(character * length)

def shape(width, tri_char, rect_height, rect_char):
    # Part 1: The Triangle
    i = 1
    while i <= width:
        line(i, tri_char)
        i += 1
    
    # Part 2: The Rectangle
    while rect_height > 0:
        line(width, rect_char)
        rect_height -= 1
