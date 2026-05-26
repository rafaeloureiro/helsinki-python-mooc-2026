"""
A function named everything_reversed, which takes a list of strings as its argument. 
The function returns a new list with all of the items on the original list reversed.
"""

def everything_reversed(my_list: list[str]):
    new_list = my_list[::-1]
    return [word[::-1] for word in new_list]
