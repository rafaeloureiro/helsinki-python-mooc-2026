"""
Add course information and export results to files.
"""

def grade(points):
    if points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    return 5


students_file = input("Student information: ")
exercises_file = input("Exercises completed: ")
exam_file = input("Exam points: ")
course_file = input("Course information: ")

# students
students = {}
with open(students_file) as file:
    next(file)
    for line in file:
        parts = line.strip().split(";")
        students[parts[0]] = f"{parts[1]} {parts[2]}"

# exercises
exercises = {}
with open(exercises_file) as file:
    next(file)
    for line in file:
        parts = line.strip().split(";")
        student_id = parts[0]
        total = sum(map(int, parts[1:]))
        exercises[student_id] = total

# exams
exam_points = {}
with open(exam_file) as file:
    next(file)
    for line in file:
        parts = line.strip().split(";")
        student_id = parts[0]
        total = sum(map(int, parts[1:]))
        exam_points[student_id] = total

# course information
with open(course_file) as file:
    lines = [line.strip() for line in file]

course_name = lines[0].split(": ", 1)[1]
credits = lines[1].split(": ", 1)[1]

# create results
txt_lines = []

header = f"{course_name}, {credits} credits"
txt_lines.append(header)
txt_lines.append("=" * len(header))
txt_lines.append(
    f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}"
    f"{'exm_pts.':10}{'tot_pts.':10}{'grade'}"
)

csv_lines = []

for student_id in students:
    name = students[student_id]

    exec_nbr = exercises.get(student_id, 0)
    exec_pts = exec_nbr // 4
    if exec_pts > 10:
        exec_pts = 10

    exm_pts = exam_points.get(student_id, 0)
    total_pts = exec_pts + exm_pts
    final_grade = grade(total_pts)

    txt_lines.append(
        f"{name:30}{exec_nbr:<10}{exec_pts:<10}"
        f"{exm_pts:<10}{total_pts:<10}{final_grade}"
    )

    csv_lines.append(
        f"{student_id};{name};{final_grade}"
    )

with open("results.txt", "w") as file:
    for line in txt_lines:
        file.write(line + "\n")

with open("results.csv", "w") as file:
    for line in csv_lines:
        file.write(line + "\n")

print("Results written to files results.txt and results.csv")
