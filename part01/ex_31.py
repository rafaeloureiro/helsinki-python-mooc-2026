"""
Bhaskara calculus using square function.
"""

from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

delta = b**2 - 4 * a * c

root1 = (-b + sqrt(delta)) / (2 * a)
root2 = (-b - sqrt(delta)) / (2 * a)

print(f"The roots are {root1} and {root2}")
