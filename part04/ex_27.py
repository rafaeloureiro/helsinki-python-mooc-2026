"""
A function named list_sum which takes two lists of integers as arguments. 
The function returns a new list which contains the sums of the items at each index in the two original lists. 
Assume both lists have the same number of items.
"""

def list_sum(list1: list[int], list2: list[int]):
    resultado = []
    
    for i in range(len(list1)):

        soma_parcial = list1[i] + list2[i]        
        resultado.append(soma_parcial)
        
    return resultado
