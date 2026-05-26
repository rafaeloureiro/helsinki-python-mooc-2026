"""
A program which asks the user to type in a sentence then prints out the first letter of each word in the sentence, each letter on a separate line.
"""

sentence = input("Please type in a sentence: ")
 
sentence = " " + sentence
 
index = 1
while index < len(sentence):
    if sentence[index-1] == " " and sentence[index] != " ":
        print(sentence[index])
    index += 1
