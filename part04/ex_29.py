"""
A function named length_of_longest, which takes a list of strings as its argument. 
The function returns the length of the longest string.
"""

def length_of_longest(mylist: list[str]):
    longest = max(mylist, key=len)
    return len(longest)
