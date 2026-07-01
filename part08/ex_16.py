"""

"""

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)

    def __str__(self):
        genre_string = ", ".join(self.genres)
        if self.ratings:
            avg = sum(self.ratings) / len(self.ratings)
            rating_str = f"{len(self.ratings)} ratings, average {avg:.1f} points"
        else:
            rating_str = "no ratings"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{rating_str}"

def minimum_grade(grade: float, series: list):
    result = []
    for s in series:
        if s.ratings and sum(s.ratings) / len(s.ratings) >= grade:
            result.append(s)
    return result

def includes_genre(genre: str, series: list):
    return [s for s in series if genre in s.genres]
