"""
A function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.
"""

def spruce(size):
    print("a spruce!")
    
    i = 1
    while i <= size:
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(f"{spaces}{stars}")
        i += 1
        
    trunk_spaces = " " * (size - 1)
    print(f"{trunk_spaces}*")
