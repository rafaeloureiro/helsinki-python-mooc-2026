"""
A program which prints out a ractangle of hash characters, the width and height are chosen by the user.
"""

width = int(input("Width: "))
height = int(input("Width: "))

while height > 0:
    print(f"{width*'#'}")
    height -= 1
