"""
The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. 
The function should print out the grid in the format specified in the examples below.

The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, 
two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. 
The function should add the digit to the specified location in the grid.
"""

def print_sudoku(sudoku: list):
    for row in range(len(sudoku)):
        for item in range(len(sudoku[row])):
            if sudoku[row][item] == 0:
                print("_", end=" ")
            else:
                print(sudoku[row][item], end=" ")
            if (item + 1) % 3 == 0 and item < 8:
                print("", end=" ")
        print()
        if (row + 1) % 3 == 0 and row < 8:
            print()

def add_number(sudoku: list, row: int, column: int, number: int):
    sudoku[row][column] = number
