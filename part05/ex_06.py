"""
A function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column_
indexes of a single square, as its arguments. Rows and columns are indexed from 0.
The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. 
That is, whether the block contains each of the numbers 1 to 9 at most once.
"""

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
