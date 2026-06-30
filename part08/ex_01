"""
A function to calculate the average of the three results for each contestant, and then return the contestant whose average result was the smallest
"""

def average(person):
    return (person["result1"] + person["result2"] + person["result3"]) / 3

def smallest_average(person1: dict, person2: dict, person3: dict):
    contestants = [person1, person2, person3]

    smallest_person = contestants[0]

    for person in contestants[1:]:
        if average(person) < average(smallest_person):
            smallest_person = person

    return smallest_person
