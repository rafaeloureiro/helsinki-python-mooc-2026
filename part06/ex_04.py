"""
A program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student.
"""

students_file = input("Student information: ")
exercises_file = input("Exercises completed: ")

students = {}
with open(students_file) as file:
    for line in file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2]

exercises = {}
with open(exercises_file) as file:
    for line in file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = sum(map(int, parts[1:]))

for student_id, name in students.items():
    total = exercises.get(student_id, 0)
    print(f"{name} {total}")
