"""
A function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, 
two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. 
The function should return a copy of the original grid with the new digit added in the correct location. 
The function should not change the original grid received as a parameter.
"""

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = [row[:] for row in sudoku]
    sudoku_copy[row_no][column_no]  = number
    return sudoku_copy
