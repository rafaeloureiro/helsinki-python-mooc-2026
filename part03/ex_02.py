"""
A program that prints a countdown starting with a giving number.
"""

print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
  print(number)
  number -= 1
print("Now!")
