"""
A program which asks for the names and ages of two persons and print out the name of the elder.
"""

print(f"Person 01")
name01 = input("Name:")
age01 = int(input("Age:"))

print(f"Person 02")
name02 = input("Name:")
age02 = int(input("Age:"))

if age01 == age02:
    print(f"{name01} and {name02} are the same age")
elif age01 > age02:
    print(f"The elder is {name01}")
elif age02 > age01:
    print(f"The elder is {name02}")
