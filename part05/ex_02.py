"""
A function which takes a two-dimensional array of integers and a single integer value as its arguments and then counts how many elements within the matrix match the argument value.
"""

def count_matching_elements(my_matrix: list, element: int) -> int:
    count = 0

    for row in my_matrix:
        for item in row:
            if item == element:
                count += 1

    return count
