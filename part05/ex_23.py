"""
A function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:

The first element in the tuple is the smallest of the arguments
The second element in the tuple is the greatest of the arguments
The third element in the tuple is the sum of the arguments
"""

def create_tuple(x: int, y: int, z: int)->tuple[int, int, int]:
   a = min(x,y,z)
   b = max(x,y,z)
   c = x + y + z
   return (a, b, c)
