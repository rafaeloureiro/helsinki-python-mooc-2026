"""
Function to get data from stations, calculate distances between stations and calculate the greatest distance between stations.
"""

import math

def get_station_data(filename: str) -> dict:
    stations = {}

    with open(filename) as file:
        next(file)

        for line in file:
            parts = line.strip().split(";")

            longitude = float(parts[0])
            latitude = float(parts[1])
            name = parts[3]
            stations[name] = (longitude, latitude)
    return stations

if __name__ == "__main__":
    get_station_data("stations1.csv")

def distance(stations: dict, station1: str, station2: str):
    lon1, lat1 = stations[station1]
    lon2, lat2 = stations[station2]

    x_km = (lon1 - lon2) * 55.26
    y_km = (lat1 - lat2) * 111.2

    return math.sqrt(x_km**2 + y_km**2)

def greatest_distance(stations: dict) -> tuple:
    max_distance = 0
    station_pair = ("", "")

    for station1 in stations:
        for station2 in stations:
            if station1 != station2:
                dist = distance(stations, station1, station2)

                if dist > max_distance:
                    max_distance = dist
                    station_pair = (station1, station2)

    return (station_pair[0], station_pair[1], max_distance)
