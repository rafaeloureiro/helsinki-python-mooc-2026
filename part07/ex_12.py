"""
A function named print_persons(filename: str), which reads a JSON file in the format, and prints the contents.
"""

import json
def print_persons(filename: str):
    with open(filename) as f:
        content = f.read()
    persons = json.loads(content)
    for person in persons:
        name = person['name']
        age = person['age']
        hobbies = ", ".join(person['hobbies'])
        print(f"{name} {age} years ({hobbies})")
