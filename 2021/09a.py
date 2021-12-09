#!/usr/bin/python3

with open('09.txt') as f:
    floor = [[int(c) for c in line.strip()] for line in f.readlines()]

s = 0

for y in range(len(floor)):
    for x in range(len(floor[0])-1):
        this = floor[y][x]
        is_low = True
        if x > 0 and floor[y][x-1] <= this:
            is_low = False
        if x < len(floor[0])-1 and floor[y][x+1] <= this:
            is_low = False
        if y > 0 and floor[y-1][x] <= this:
            is_low = False
        if y < len(floor)-1 and floor[y+1][x] <= this:
            is_low = False

        if is_low:
            print(x,y)
            s += this + 1

print(s)
