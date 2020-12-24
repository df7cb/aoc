#!/usr/bin/python3

import re

floor = set() # x,y; rows shifted such that 0,1 is NE of 0,0 and 0,-1 is SW

def explode(line):
    m = re.findall('(e|se|sw|w|nw|ne)', line)
    return m

def walk(path):
    x, y = 0, 0
    for direction in path:
        if direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
        elif direction == 'ne':
            y += 1
        elif direction == 'nw':
            x -= 1
            y += 1
        elif direction == 'se':
            x += 1
            y -= 1
        elif direction == 'sw':
            y -= 1
    return x, y

with open('24.txt') as f:
    for line in f:
        path = explode(line)
        tile = walk(path)
        print(line.strip(), path, tile)
        if tile in floor:
            floor.remove(tile)
        else:
            floor.add(tile)

print('24a:', len(floor))

def neighbors(floor, x, y):
    n = 0
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (-1, 1), (1, -1), (0, -1)):
        if (x+dx, y+dy) in floor:
            n += 1
    return n

def life(floor):
    min_x = min(t[0] for t in floor)
    max_x = max(t[0] for t in floor)
    min_y = min(t[1] for t in floor)
    max_y = max(t[1] for t in floor)

    floor2 = set()
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            n = neighbors(floor, x, y)
            if (x, y) in floor and (n == 1 or n == 2):
                floor2.add((x, y))
            if (x, y) not in floor and n == 2:
                floor2.add((x, y))

    return floor2

for i in range(1, 101):
    floor = life(floor)
    print(i, len(floor))
