#!/usr/bin/python3

import sys
sys.setrecursionlimit(100000)

with open("23.txt") as f:
    trail = [list(line.strip()) for line in f]

def print_trail(trail):
    for line in trail:
        print(line)

y, x = 0, 1
my = len(trail)
mx = len(trail[0])

print_trail(trail)
best = 0

def walk(trail, path, y, x):
    if (y, x) == (my-1, mx-2):
        global best
        best = max(best, path)
        print(y, x, path, best) # ignore start
        return

    for y2, x2 in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
        if y2 < 0 or y2 >= my or x < 0 or x >= mx:
            continue

        t2 = trail[y2][x2]
        if t2 == '#': continue

        #if path[-1] == (y2, x2): contine
        #if (y2, x2) in path: continue

        trail[y2][x2] = '#'
        walk(trail, path + 1, y2, x2)
        trail[y2][x2] = '.'

trail[y][x] = '#'
walk(trail, 0, y, x)
print(best)
