"""
Implementing other methods for two classes and __str__
"""

class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        return self.people == []

    def print_contents(self):
        if len(self.people) >= 1:
            print(f"There are {len(self.people)} persons in the room, and their combined height is {sum(person.height for person in self.people)} cm")
            for person in self.people:
                print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if not self.people:
            return None
        shortest_person = self.people[0]
        for person in self.people:
            if person.height < shortest_person.height:
                shortest_person = person
        return shortest_person

    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person is None:
            return None
        self.people.remove(shortest_person)
        return shortest_person
