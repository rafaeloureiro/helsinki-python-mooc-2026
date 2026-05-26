"""
A program which asks the user for a string then prints out a message based on whether the second character and the second to last character are the same or not.
"""

input01 = str(input("Please type in a string: "))
index = len(input01)-2
if input01[1] == input01[index]:
  print(f"The second and the second to last characters are {input01[index]}")
else:
  print(f"The second and the second to last characters are different")
