"""
Continuation of the two prior exercises including statistics print.
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

print(f"{'name'}{' '*26}{'exec_nbr'}{' '*2}{'exec_pts.'}{' '*1}{'exm_pts.'}{' '*2}{'tot_pts.'}{' '*2}{'grade'}{' '*5}")

for student_id, name in students.items():
    exec_nbr = exercises.get(student_id, 0)
    ex_pts = exercise_points(exec_nbr)
    exam_pts = exam.get(student_id, 0)
    total = ex_pts + exam_pts
    g = grade(total)
    print(f"{name}{(30 - len(name))* ' '}{exec_nbr}{(10-len(str(exec_nbr)))*' '}{ex_pts}{(10-len(str(ex_pts)))*' '}{exam_pts}{(10-len(str(exam_pts)))*' '}{total}{(10-len(str(total)))*' '}{g}{(10-len(str(g)))*' '}")
