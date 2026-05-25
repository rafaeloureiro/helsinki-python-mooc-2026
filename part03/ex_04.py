"""
A program which asks the user to type in an upper limit then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. 
The program prints out powers of two in order.
The execution of the program finishes when the next number to be printed would be greater than the limit set by the user.
"""

limit = int(input("Upper limit: "))
number = 1
while number <= limit:
    print(number)
    number *= 2
