"""
A function named read_input, which asks the user for input until the user types in an integer which falls within the bounds given as arguments to the function.
"""

def read_input(prompt: str, lower: int, upper: int):
    
    while True:
        try:
            number = int(input(prompt))

            if lower <= number <= upper:
                return number

            print(f"You must type in an integer between {lower} and {upper}")

        except ValueError:
            print(f"You must type in an integer between {lower} and {upper}")
