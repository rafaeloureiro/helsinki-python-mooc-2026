"""
A function named oldest_person(people: list), which takes a list of tuples as its argument. 
In each tuple, the first element is the name of a person, and the second element is their year of birth. 
The function should find the oldest person on the list and return their name.
"""

def oldest_person(people: list):
    oldest = people[0]
    for person in people:
        # comparing the year of birth of the oldest known person and the person in turn
        if person[1] < oldest[1]:
            oldest = person
 
    return oldest[0]
