"""
A function named filter_incorrect(), which creates a file called correct_numbers.csv. 
The file should contain only those lines from the original file which are in the correct format.
The file lottery_numbers.csv containts winning lottery numbers in the following format:
Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.
The file has been corrupted. Lines in the file may contain errors
"""

def filter_incorrect():

    with open("lottery_numbers.csv") as source, open("correct_numbers.csv", "w") as target:

        for line in source:
            line = line.strip()

            try:
                week_part, numbers_part = line.split(";")

                week = week_part.split()

                if len(week) != 2:
                    continue

                if week[0] != "week":
                    continue

                int(week[1])

                numbers = numbers_part.split(",")

                if len(numbers) != 7:
                    continue

                numbers = [int(number) for number in numbers]

                if not all(1 <= number <= 39 for number in numbers):
                    continue

                if len(numbers) != len(set(numbers)):
                    continue

                target.write(line + "\n")

            except ValueError:
                continue
