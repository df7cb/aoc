#!/usr/bin/python3

with open('11.txt') as f:
    dumbos = [[int(x) for x in line.strip()] for line in f]

def dump(dumbos):
    for line in dumbos:
        print("".join([str(x) for x in line]))

dump(dumbos)

def inc(dumbos, y, x):
    dumbos[y][x] += 1
    if dumbos[y][x] == 10:
        return 1 + flash(dumbos, y, x)
    return 0

def flash(dumbos, y, x):
    flashes = 0
    if y > 0:
        if x > 0:
            flashes += inc(dumbos, y-1, x-1)
        flashes += inc(dumbos, y-1, x)
        if x < len(dumbos[0])-1:
            flashes += inc(dumbos, y-1, x+1)
    if x > 0:
        flashes += inc(dumbos, y, x-1)
    if x < len(dumbos[0])-1:
        flashes += inc(dumbos, y, x+1)
    if y < len(dumbos)-1:
        if x > 0:
            flashes += inc(dumbos, y+1, x-1)
        flashes += inc(dumbos, y+1, x)
        if x < len(dumbos[0])-1:
            flashes += inc(dumbos, y+1, x+1)
    return flashes

def step(dumbos):
    flashes = 0
    for y in range(len(dumbos)):
        for x in range(len(dumbos[0])):
            flashes += inc(dumbos, y, x)
    for y in range(len(dumbos)):
        for x in range(len(dumbos[0])):
            if dumbos[y][x] >= 10:
                dumbos[y][x] = 0
    return flashes

for i in range(1, 10000):
    flashes = step(dumbos)
    print(i, flashes)
    if flashes == 100:
        break

dump(dumbos)
