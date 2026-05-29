"""
Checks if a specific column in a Sudoku grid is filled in correctly.

A function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument. 
The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. 
Copy the functions from the exercises above into your Python code file for this exercise.

The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the numbers 1 to 9 at most once, the function returns True. 
If a single one is filled in incorrectly, the function returns False.
"""

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True

def block_correct(sudoku: list, row_no:int, column_no:int):
    numbers = []
    for row in sudoku[row_no:row_no+3]:
        for number in row[column_no:column_no+3]:
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True

def row_correct(sudoku: list, row_no: int):
    # Get the specific row we want to check using its index
    row = sudoku[row_no]
    
    # Track the numbers we have already seen in this row
    seen_numbers = []
    
    for item in row:
        if item == 0:
            continue
            
        if item in seen_numbers:
            return False
            
        seen_numbers.append(item)
        
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False
            
    for row_no in range(0, 9, 3):
        for column_no in range(0, 9, 3):
            if not block_correct(sudoku, row_no, column_no):
                return False
            
    return True
