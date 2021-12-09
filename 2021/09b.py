#!/usr/bin/python3

with open('09.txt') as f:
    floor = [[int(c) for c in line.strip()] for line in f.readlines()]

def basin(floor, x, y):
    r = 1
    floor[y][x] = 9
    if x > 0 and floor[y][x-1] != 9:
        r += basin(floor, x-1, y)
    if x < len(floor[0])-1 and floor[y][x+1] != 9:
        r += basin(floor, x+1, y)
    if y > 0 and floor[y-1][x] != 9:
        r += basin(floor, x, y-1)
    if y < len(floor)-1 and floor[y+1][x] != 9:
        r += basin(floor, x, y+1)
    return r

basins = []

for y in range(len(floor)):
    for x in range(len(floor[0])):
        if floor[y][x] != 9:
            b = basin(floor, x, y)
            print(x, y, b)
            basins.append(b)

basins.sort()
print(basins[-3:])
print(basins[-3] * basins[-2] * basins[-1])
