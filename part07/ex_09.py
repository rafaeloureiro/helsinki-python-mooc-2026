"""
A program which asks the user for their date of birth, and then prints out how old the user was on the eve of the new millennium.
"""

from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birthday = datetime(year, month, day)
millennium_eve = datetime(1999, 12, 31)

if birthday > millennium_eve:
    print("You weren't born yet on the eve of the new millennium.")
else:
    age_in_days = (millennium_eve - birthday).days
    print(f"You were {age_in_days} days old on the eve of the new millennium.")