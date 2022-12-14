#!/usr/bin/python3

import re

max_x, max_y = 0, 0
start_x, start_y = 500, 0

structure = []

with open("14.txt") as f:
    for line in f:
        coords = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in line.split(' -> ')]
        for c in coords:
            max_x = max(c[0], max_x)
            max_y = max(c[1], max_y)
        structure.append(coords)

def print_rock(rock):
    for line in rock:
        print(''.join(line))

print(max_x, max_y)
rock = [['.' for i in range(max_x*2)] for j in range(max_y+2)]
rock.append(['#' for i in range(max_x*2)])

for s in structure:
    for i in range(len(s)-1):
        x0, y0 = s[i]
        x1, y1 = s[i+1]
        if (x0 == x1):
            for y in range(min(y0, y1), max(y0, y1)+1):
                rock[y][x0] = '#'
        elif (y0 == y1):
            for x in range(min(x0, x1), max(x0, x1)+1):
                rock[y0][x] = '#'
        else:
            raise Exception('structure is weird')

print_rock(rock)

def drop_sand(rock):
    x, y = start_x, start_y
    if rock[y][x] == 'o':
        return False
    while True:
        if y == len(rock)-1:
            print('The End')
            return False
        if rock[y+1][x] == '.':
            y += 1
        elif rock[y+1][x-1] == '.':
            y += 1
            x -= 1
        elif rock[y+1][x+1] == '.':
            y += 1
            x += 1
        else:
            rock[y][x] = 'o'
            return True

drops = 0
while drop_sand(rock):
    drops += 1
    print(drops)

print_rock(rock)
print(drops)
