"""
A function named store_personal_data(person: tuple), which takes a tuple containing some identifying information as its argument.
This should be processed and written into the file people.csv. 
The file may already contain some data; the new entry goes to the end of the file. The data should be written in the format: name;age;height
"""

def store_personal_data(person: tuple):
    name, age, height = person

    with open("people.csv", "a") as file:
        file.write(f"{name};{age};{height}\n")
