"""
A program that print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish. 
"""

while True:
    print("hi")
    ask = input("Shall we continue? ")
    if ask.lower() == "no":
        print("okay then")
        break
