"""
A function named fractionate(amount: int), which takes the number of parts as its argument. 
The function should divide the number 1 into as many equal sized fractions as is specified by the argument, and return these in a list.
"""

from fractions import Fraction

def fractionate(amount: int) -> list:
    fraction = Fraction(1,amount)

    return [fraction] * amount
