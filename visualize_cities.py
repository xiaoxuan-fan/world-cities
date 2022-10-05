# Author: Xiaoxuan
# Date: 5/25/2021
# Purpose: visualize the 50 most populous cities on a world map
from cs1lib import *
n_cities = 1  # number of cities that are drawn in each call
WIN_WIDTH = 720
WIN_HEIGHT = 360
FRAMERATE = 1
DOT_RADIUS = 3


LIMIT = 50  # total number of cities we want to draw
mycities = []
count = 0
fp = open('cities_population.txt', 'r')
for line in fp:
    if count == LIMIT:
        break
    info = line.split(',')
    mycities.append((float(info[2]), float(info[3])))
    count += 1
fp.close()


def main_draw():
    global n_cities
    img = load_image('world.png')
    draw_image(img, 0, 0)

    disable_stroke()
    set_fill_color(1, 0, 1)

    for i in range(n_cities):
        latitude, longitude = mycities[i]
        x = (180 + longitude) * WIN_WIDTH / 360
        y = (90 - latitude) * WIN_HEIGHT / 180
        draw_circle(x, y, DOT_RADIUS)
    if n_cities < LIMIT:
        n_cities += 1


start_graphics(main_draw, width=WIN_WIDTH, height=WIN_HEIGHT, framerate=FRAMERATE)
