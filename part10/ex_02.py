"""
A GameWarehouse object is used to store ComputerGame objects.
A class named GameMuseum which inherits the GameWarehouse class.
The GameMuseum class override the list_games() method and returns a list of only those games which were made before the year 1990.
The class GameMuseum also have a constructor which calls the constructor from the parent class GameWarehouse. The constructor takes no arguments.
"""

class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games
    
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()  

    def list_games(self):
        old_games = []
        for games in super().list_games():
            if games.year < 1990:
                old_games.append(games)
        return old_games
