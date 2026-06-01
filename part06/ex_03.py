"""
Theree functions:
- matrix_sum
return the sum of the elements in the matrix
- matrix_max
return the element with the greatest value in the matrix
- row_sums
returns a list containing the sum of each row in the matrix
"""

def read_matrix():
    matrix = []
    with open('matrix.txt') as file:
        for line in file:
            row = list(map(int, line.strip().split(",")))
            matrix.append(row)
        return matrix

def row_sums():
    matrix = read_matrix()
    return [sum(row) for row in matrix]

def matrix_sum():
    matrix = read_matrix()
    return sum(sum(row) for row in matrix)

def matrix_max():
    matrix = read_matrix()
    return max(max(row) for row in matrix)
