"""
A function that transpose a given matrix.
Assume that the matrix is a square matrix.
"""

def transpose(matrix: list):
    transposed = []
    
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transposed.append(row)
    matrix[:] = transposed
