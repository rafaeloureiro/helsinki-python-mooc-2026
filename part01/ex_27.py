"""
A program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius.
"""

temperature = int(input("Please type in a temperature (F):"))
celsius = (temperature -32)/1.8
print(f"{temperature} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print(f"Brr! It's cold in here!")
