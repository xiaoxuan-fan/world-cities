# Author: Xiaoxuan
# Date: 5/25/2021
# Purpose: read in city info, sort the cities based on different criteria and write to output files
from city import City
from quicksort import sort


def compare_names(c1, c2):
    return c1.name.lower() <= c2.name.lower()


def compare_population(c1, c2):
    return c2.population <= c1.population


def compare_latitude(c1, c2):
    return c1.latitude <= c2.latitude


mycities = []
fp = open('world_cities.txt', 'r')
for line in fp:
    info = line.strip().split(',')
    city = City(info[0], info[1], info[2], int(info[3]), float(info[4]), float(info[5]))
    mycities.append(city)
fp.close()

sort(mycities, compare_names)

fp = open('cities_alpha.txt', 'w')
for city in mycities:
    fp.write(str(city) + '\n')
fp.close()

sort(mycities, compare_population)

fp = open('cities_population.txt', 'w')
for city in mycities:
    fp.write(str(city) + '\n')
fp.close()

sort(mycities, compare_latitude)

fp = open('cities_latitude.txt', 'w')
for city in mycities:
    fp.write(str(city) + '\n')
fp.close()
