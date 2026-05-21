"""
A program which asks for the number of students on a course and the desired group size. 
The program will then print out the number of groups formed from the students on the course. 
If the division is not even, one of the groups may have fewer members than specified.
"""

students_course = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

groups = (students_course + group_size - 1) // group_size

print(f"Number of groups formed: {groups}")
