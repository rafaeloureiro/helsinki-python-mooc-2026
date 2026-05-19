"""
A function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list
"""
def longest(strings: list) -> str:
    longest_string = ""

    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string

