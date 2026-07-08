"""
Encapsulated attributes in different methods within a single class
"""

class WeatherStation:
    def __init__(self, station):
        self.__station = station
        self.__entries = []
    
    def add_observation(self, observation: str):
        self.__entries.append(observation)

    def latest_observation(self):
        if self.__entries:
            return self.__entries[-1]
        return ""
    
    def number_of_observations(self):
        return len(self.__entries)

    def __str__(self):
        return f"{self.__station}, {self.number_of_observations()} observations"
