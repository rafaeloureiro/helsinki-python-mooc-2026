"""
A program which first asks the user for the number of items to be added. 
Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. 
Finally, the list is printed out.
"""

my_list = []
num_items = int(input("How many items: "))

while num_items > 0:
    item = int(input(f"Item {num_items}: "))
    my_list.append(item)
    num_items -= 1

print(my_list)
