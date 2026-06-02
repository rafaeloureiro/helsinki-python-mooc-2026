"""
Continuation of the prior exercise including exam, grades and total_points.
"""

students_file = input("Student information: ")
exercises_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

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

exam = {}
with open(exam_file) as file:
    for line in file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exam[parts[0]] = sum(map(int, parts[1:]))

def exercise_points(total):
    return min(10, total // 4) 

def grade(total_points):
    if total_points < 15:
        return 0
    elif total_points < 18:
        return 1
    elif total_points < 21:
        return 2
    elif total_points < 24:
        return 3
    elif total_points < 28:
        return 4
    else:
        return 5

for student_id, name in students.items():
    ex_points = exercise_points(exercises.get(student_id, 0))
    exam_points = exam.get(student_id, 0)
    total = ex_points + exam_points
    print(f"{name} {grade(total)}")
