"""
A class named Square which inherits the Rectangle class. 
The sides of a square are all of equal length, which makes the square a special case of the rectangle. 
The new class should not contain any new attributes.
"""

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def __str__(self):
        return f"square {self.width}x{self.height}"
