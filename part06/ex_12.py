"""
A solution filtering for correct and incorrect math answers.
"""

def filter_solutions():
    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for row in source:
            # Split into pieces
            pieces = row.split(";")
 
            calculation = pieces[1]
            result = pieces[2]
 
            if "+" in calculation:
                operands = calculation.split("+")
                correct = int(operands[0]) + int(operands[1]) == int(result)
            else:
                operands = calculation.split("-")
                correct = int(operands[0]) - int(operands[1]) == int(result)
 
            if correct:
                correct_file.write(row)
            else:
                incorrect_file.write(row)
