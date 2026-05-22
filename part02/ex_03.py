"""
A program which asks the user for a floating point number and then prints out the integer part and the decimal part separately.
"""

number = float(input("Please type in a number: "))
integer_number = int(number)
decimal_part = number - integer_number
print(f"Integer part: {integer_number}")
print(f"Decimal part: {decimal_part}")
