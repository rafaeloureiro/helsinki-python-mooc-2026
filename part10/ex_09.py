"""
ShoppingList class: represents a shopping list.

Stores products as (name, quantity) pairs and allows:
- adding items to the list (add);
- checking the total number of items (number_of_items);
- accessing a product's name or quantity by its position number, starting at 1 (product, number);
- iterating directly over the object with a for loop, yielding each item as a (product, quantity) tuple.
"""
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]
    
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n >= len(self.products):
            raise StopIteration
        product = self.products[self.n]
        self.n += 1
        return product
