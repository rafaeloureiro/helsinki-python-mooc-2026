"""
A function named hypotenuse(leg1: float, leg2: float), which takes the lengths of the two sides adjacent to the right angle of an orthogonal triangle. 
The function should return the length of the hypotenuse, or the side opposite to the right angle.
"""

from math import * 

def hypotenuse(leg1: float, leg2: float):
    return sqrt(leg1**2 + leg2**2)
