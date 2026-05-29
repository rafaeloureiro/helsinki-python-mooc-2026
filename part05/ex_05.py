"""
Checks if a specific column in a Sudoku grid is filled in correctly.

A column is valid if it contains each of the numbers 1 to 9 at most once. 
Empty squares (represented by 0) are ignored and can appear multiple times.
"""
def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
