"""
A program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:
- in the order the items were added
- ordered from smallest to greatest
The program exits when the user types in 0.
"""

numbers = []

while True:
    new = int(input("New item: "))

    if new == 0:
        print("Bye!")
        break   

    numbers.append(new)
    print(f"The list now: {numbers}")
    print(f"The list in order: {sorted(numbers)}")
