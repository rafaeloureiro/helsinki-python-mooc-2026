"""
A program which asks the user to type in an upper limit and a number then prints out numbers so that each subsequent number is the previous number one doubled, starting from the number 1. 
The program prints out powers of n in order.
The execution of the program finishes when the next number to be printed would be greater than the limit set by the user.
"""

limit = int(input("Upper limit: "))
multiplier = int(input("Base: "))

number = 1
while number <= limit:
    print(number)
    number *= multiplier
