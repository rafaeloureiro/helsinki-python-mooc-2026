"""
A program which asks the user to type in a number then prints out all the positive integer values from 1 up to the number. 
However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth.
"""

limit = int(input("Please type in a number: "))
i = 1

while i <= limit:
    if i + 1 <= limit:
        print(i + 1)
        print(i)
    else:
        print(i)
    
    i += 2
