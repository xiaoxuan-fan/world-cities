# Author: Xiaoxuan
# Date: 5/19/2021
# Purpose: read from world_cities.txt, create city objects, and write to cities_out.txt
from city import City

fp = open('world_cities.txt', 'r')
mycities = []
for line in fp:
    info = line.strip().split(',')
    city = City(info[0], info[1], info[2], int(info[3]), float(info[4]), float(info[5]))
    mycities.append(city)
fp.close()

fp = open('cities_out.txt', 'w')
for city in mycities:
    fp.write(str(city) + '\n')
fp.close()
