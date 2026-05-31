"""
A function named older_people(people: list, year: int), which selects all those people on the list who were born before the year given as an argument. 
The function should return the names of these people in a new list.
"""

def older_people(people: list, year: int):
    older = []
    for person in people:
        if person[1] < year:
            older.append(person[0])
    return older
