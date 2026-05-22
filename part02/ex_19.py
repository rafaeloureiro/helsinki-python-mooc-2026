"""
A program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. 
The program should then print out the number of times the user tried different codes.
"""

PIN = 4321
chances = 1
input_PIN = int(input("PIN: "))

while input_PIN != PIN:
    chances += 1
    print("Wrong")
    input_PIN = int(input("PIN: "))
if chances == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {chances} attempts")
