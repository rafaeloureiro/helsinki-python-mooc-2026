"""
A class named Person with a single attribute name with two methods:

The method return_first_name should return the first name of the person, while the method return_last_name should return the last name of the person.
"""

class Person:
    def __init__(self, name: str):
        self.name = name

    def return_first_name (self):
        names = self.name.split()
        return names[0]
    
    def return_last_name (self):
        names = self.name.split()
        return names[-1]
