"""
A program which asks the user to type in a number then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range.
"""

limit = int(input("Please type in a number: "))

left = 1
right = limit

while left <= right:
    print(left)
    left += 1
    
    if left <= right:
        print(right)
        right -= 1
