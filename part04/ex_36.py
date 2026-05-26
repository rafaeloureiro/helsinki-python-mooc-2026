"""
A function named no_shouting, which takes a list of strings as an argument. 
The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.
"""

def no_shouting(my_list: list[str]):
    new_list = []
    for char in my_list:
        if not char.isupper():
            new_list.append(char)
    return new_list
