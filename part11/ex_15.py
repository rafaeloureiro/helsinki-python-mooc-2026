"""
Function balanced_brackets which takes a string as its argument. 
It checks if the brackets, or parentheses, within the string are balanced. That is, for each opening bracket ( there should be a closing bracket ), and
all pairs of brackets should be matched in order, i.e. the bracket pairs must not be crossed.
"""

def balanced_brackets(my_string: str) -> bool:
    my_string = "".join(char for char in my_string if char in "()[]")

    if len(my_string) == 0:
        return True

    pairs = {"(": ")", "[": "]"}

    if my_string[0] not in pairs or my_string[-1] != pairs[my_string[0]]:
        return False

    return balanced_brackets(my_string[1:-1])
