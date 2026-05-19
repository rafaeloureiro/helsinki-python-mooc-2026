"""
Checks if a specific row in a Sudoku grid is filled in correctly.

A row is valid if it contains each of the numbers 1 to 9 at most once. 
Empty squares (represented by 0) are ignored and can appear multiple times.
"""
def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    
    seen_numbers = []
    
    for item in row:
        if item == 0:
            continue
            
        if item in seen_numbers:
            return False
            
        seen_numbers.append(item)
        
    return True
