"""
A program which asks the user to choose between addition and removal. 
Depending on the choice, the program adds an item to or removes an item from the end of a list. 
The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.
"""

items = []

while True:
    print(f"The list is now {items}")
    choice = input("a(d)d, (r)emove or e(x)it: ").lower()

    if choice == 'd':
        if len(items) == 0:
            items.append(1)
        else:
            new_item = items[-1] + 1
            items.append(new_item)
            
    elif choice == 'r':
        if len(items) > 0:
            items.pop()
            
    elif choice == 'x':
        break

print("Bye!")
