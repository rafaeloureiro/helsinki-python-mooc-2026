"""
A program which asks for the amount of points received and then prints out the grade attained according to the table.
"""

grade = int(input(f"How many points [0-100]:"))
if grade<0:
    print(f"Grade: impossible!")
elif 0<grade<=49:
    print(f"Grade: fail")
elif 50<=grade<=59:
    print(f"Grade: 1")
elif 60<=grade<=69:
    print(f"Grade: 2")
elif 70<=grade<=79:
    print(f"Grade: 3")
elif 80<=grade<=89:
    print(f"Grade: 4")
elif 90<=grade<=100:
    print(f"Grade: 5")
elif grade>100:
    print(f"Grade: impossible!")
