# Author: Xiaoxuan
# Date: 5/19/2021
# Purpose: define a City class to store information about cities
class City:
    def __init__(self, country, name, region, population, latitude, longitude):
        self.country = country
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return self.name + ',' + str(self.population) + ',' + str(self.latitude) + ',' + str(self.longitude)
