"""
A program which asks for the hourly wage, hours worked, and the day of the week. 
The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.
"""

wage = float(input("Hourly wage:"))
hours = float(input("Hours worked:"))
weekday = input("Day of the week:")
if weekday == "Sunday":
    print(f"Daily wages: {(wage*2)*hours} euros")
else:
    print(f"Daily wages: {wage*hours} euros")
