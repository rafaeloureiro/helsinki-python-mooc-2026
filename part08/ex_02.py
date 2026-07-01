"""
A function which adds a new element on each row in the matrix. 
This element contains the sum of the other elements on that row.
"""

def row_sums(my_matrix: list):

    for row in my_matrix:
        row.append(sum(row))
