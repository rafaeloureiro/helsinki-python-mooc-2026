"""
A program which prints out all the even numbers between two and thirty, using a loop. 
Each number is printed on a separate line.
"""

number = 2
while number <= 30:
  if number % 2 == 0:
    print(f"{number}")
  number += 1
