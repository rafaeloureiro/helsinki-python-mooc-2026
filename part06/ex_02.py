"""
A function named read_fruits, which reads the file and returns a dictionary based on the contents. 
In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.
"""

def read_fruits():
    fruits = {}
    with open('fruits.csv') as file:
        for line in file:
            fruit, fruit_price = line.strip().split(';')
            fruits[fruit] = float(fruit_price)
    return fruits  
