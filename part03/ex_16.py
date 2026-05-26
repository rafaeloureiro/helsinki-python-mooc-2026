"""
A program which asks the user for a string and then prints out a frame of * characters with the word in the centre. 
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.
If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.
"""

word = str(input("Please type in a string: "))
space = 30 - (len(word)) - 2
side_space = space // 2

print(f"{'*'*30}")
print(f"*{' ' * side_space}{word}{' ' * (space - side_space)}*")
print(f"{'*'*30}")
