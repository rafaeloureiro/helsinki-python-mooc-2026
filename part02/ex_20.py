"""
A program which asks the user for a year, and prints out the next leap year.
If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year.
"""

year = int(input("Year: "))
current_year = year

while True:
    current_year += 1
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        print(f"The next leap year after {year} is {current_year}")
        break
