"""
A function named all_the_longest, which takes a list of strings as its argument. 
The function should return a new list containing the longest string in the original list. 
If more than one are equally long, the function should return all of the longest strings.
The order of the strings in the returned list should be the same as in the original.
"""

def all_the_longest(names: list):
    result = []
 
    for name in names:
        if result == [] or len(name) > len(result[0]):
            result = [name]
        elif len(name) == len(result[0]):
            result.append(name)
 
    return result

