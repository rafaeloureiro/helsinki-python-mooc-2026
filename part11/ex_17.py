"""
A function named count_subordinates(employee: Employee) which recursively counts the number of subordinates each employee has.
"""

class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee) -> int:
    total = len(employee.subordinates)
    for subordinate in employee.subordinates:
        total += count_subordinates(subordinate)
    return total
