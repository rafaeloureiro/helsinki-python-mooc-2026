"""

"""

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

    def __repr__(self):
        return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"

def books_of_genre(books: list, genre: str):
    list_by_genre=[]

    for book in books:
        if book.genre == genre:
            list_by_genre.append(book)
    return list_by_genre
