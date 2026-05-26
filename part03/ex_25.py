"""
A program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. 
Otherwise the program prints out the factorial of the number.
"""

while True:
    number = int(input("Please type in a number: "))
    if number <=0:
      print("Thanks and bye!")
      break

    current_factorial = 1
    counter = 1
    while counter <= number:
        current_factorial *= counter
        counter += 1

    print(f"The factorial of the number {number} is {current_factorial}")
