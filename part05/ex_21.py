"""
A function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.
"""

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    database.append({"name": name, "director": director, "year": year, "runtime": runtime})
