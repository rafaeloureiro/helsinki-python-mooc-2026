"""
Checks if a specific column in a Sudoku grid is filled in correctly.

A column is valid if it contains each of the numbers 1 to 9 at most once. 
Empty squares (represented by 0) are ignored and can appear multiple times.
"""
def column_correct(sudoku: list, column_no: int):
    column = sudoku[row_no]
    
    seen_numbers = []
    
    for item in column:
        if item == 0:
            continue
            
        if item in seen_numbers:
            return False
            
        seen_numbers.append(item)
        
    return True
