"""
A function named triangle, which draws a triangle of hashes, and takes one argument. 
The triangle should be as tall and as wide as the value of the argument.
The function should call the function line from the exercise prior for the actual printing out. 
Copy your solution to that exercise prior the code for this exercise. Please don't change anything in the line function.
"""

def line(length, text):
    if text == "":
        character = "*"
    else:
        character = text[0]
    
    print(f"{character * length}")

def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1
