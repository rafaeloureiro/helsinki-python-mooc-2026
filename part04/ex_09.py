"""
A function named greatest_number, which takes three arguments. The function returns the greatest in value of the three.
"""

def greatest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
