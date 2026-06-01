"""
A function named largest, which reads the file and returns the largest number in the file.
"""

def largest():
    with open("numbers.txt") as new_file:
        largest = None

        for number in new_file:
            number = int(number.strip())
            if largest is None or number > largest:
                largest = number
    return largest
