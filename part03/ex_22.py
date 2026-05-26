"""
A program which finds the second occurrence of a substring. 
If there is no second (or first) occurrence, the program should print out a message accordingly.
In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.
"""

text = input("Please type in a string: ")
sub = input("Please type in a substring: ")

index1 = text.find(sub)

if index1 != -1:
    index2 = text.find(sub, index1 + len(sub))
    
    if index2 != -1:
        print(f"The second occurrence of the substring is at index {index2}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")
