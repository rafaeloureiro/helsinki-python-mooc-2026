"""
A class named SuperGroup which represents a group of superheroes. 

It contains Protected attributes name (str), location (str) and members (list),
A constructor which takes the name and location of the group as arguments, in that order,
Getter methods for the name and location attributes,
A method named add_member(hero: SuperHero) which adds a new member to the group,
A method named print_group which prints out information about the group and its members.
"""

class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup:
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    def add_member(self, member: SuperHero):
        self._members.append(member)

    def print_group(self):
        print(f"{self._name}, {self._location}")
        print("Members:")
        for member in self._members:
            print(member)
