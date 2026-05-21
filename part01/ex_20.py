"""
A program which estimates a user's typical food expenditure.

The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

Based on this information the program calculates the user's typical food expenditure both weekly and daily.
"""
week = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
budget = float(input("How much money do you spend on groceries in a week? "))

daily_average = (week * price + budget) / 7
weekly_average = week * price + budget

print(f"Average food expenditure:")
print(f"Daily: {daily_average} euros")
print(f"Weekly: {weekly_average} euros")
