"""
A program which asks the user to input a string then prints out different messages if the string contains any of the vowels a, e or o.
Assume the input will be in lowercase entirely.
"""

word = input("Please type in a string: ")

string = input("Please type in a string: ")
vowels = "aeo"
index = 0
 
while index < len(vowels):
    vowel = vowels[index]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1
