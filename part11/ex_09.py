"""
A function named products_in_shopping_list(shopping_list, amount: int) which takes a ShoppingList object and an integer value as its arguments. 
The function returns a list of product names. The list should include only the products with at least the number of items specified by the amount parameter.
"""

class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]
            self.n += 1
            return product
        else:
            raise StopIteration
        
def products_in_shopping_list(shopping_list, amount: int) -> list:
    return [product for product, number in shopping_list if number >= amount]
