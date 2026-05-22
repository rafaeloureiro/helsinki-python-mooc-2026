"""
A program which asks the user for integer numbers and keep asking for numbers until the user types in zero.
After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.
The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.
The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.
The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.
"""

print("Please type in integer numbers. Type in 0 to finish.")
numbers = 0
sum = 0
positives = 0
 
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    numbers += 1
    sum += number
    if number>0:
        positives += 1
 
print("Numbers typed in", numbers)
print("The sum of the numbers is", sum)
print("The mean of the numbers is", sum/numbers)
print("Positive numbers", positives)
print("Negative numbers", numbers-positives)
