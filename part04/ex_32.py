"""
A function named formatted, which takes a list of floating point numbers as its argument. 
The function returns a new list, which contains each element of the original list in string format, rounded to two decimal points.
"""

def formatted(mylist: list[float]):
    new = [f"{x:.2f}" for x in mylist]
    return new
