"""
A program which calculates the correct amount of tax for a gift from a close relative. 
"""

present_value = int(input("Value of gift: "))

if present_value <= 5000:
    print("No tax")
elif present_value <= 25000:
    tax = 100 + (present_value - 5000) * 0.08
    print(f"Amount of tax: {int(tax)} euros")
elif present_value <= 55000:
    tax = 1700 + (present_value - 25000) * 0.10
    print(f"Amount of tax: {int(tax)} euros")
elif present_value <= 200000:
    tax = 4700 + (present_value - 55000) * 0.12
    print(f"Amount of tax: {int(tax)} euros")
elif present_value <= 1000000:
    tax = 22100 + (present_value - 200000) * 0.15
    print(f"Amount of tax: {int(tax)} euros")
else:
    tax = 142100 + (present_value - 1000000) * 0.17
    print(f"Amount of tax: {int(tax)} euros")
