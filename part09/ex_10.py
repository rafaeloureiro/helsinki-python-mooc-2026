"""
Initializing attributes through getter and setter methods
"""

class Recording:
    def __init__(self, length: int):
        if length < 0:
            raise ValueError
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length: int):
        if new_length < 0:
            raise ValueError
        self.__length = new_length
