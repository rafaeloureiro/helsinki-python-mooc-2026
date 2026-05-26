"""
A function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.
"""

def longest_series_of_neighbours(my_list: list[int]):

    if len(my_list) < 2:
        return len(my_list)
        
    longest = 1 
    current = 1 
    
    for i in range(len(my_list) - 1):
        if abs(my_list[i] - my_list[i + 1]) == 1:
            current += 1 
        else:
            current = 1 
            
        if current > longest:
            longest = current
            
    return longest
