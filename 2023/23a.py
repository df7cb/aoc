#!/usr/bin/python3

import sys
sys.setrecursionlimit(100000)

with open("23.txt") as f:
    trail = [line.strip() for line in f]

def print_trail(trail):
    for line in trail:
        print(line)

y, x = 0, 1

print_trail(trail)
best = 0

def walk(trail, path, y, x):
    if (y, x) == (len(trail)-1, len(trail[0])-2):
        print(y, x, len(path)-1) # ignore start
        global best
        best = max(best, len(path)-1)
        return

    for y2, x2 in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
        if y2 < 0 or y2 >= len(trail) or x < 0 or x >= len(trail[0]):
            continue

        t2 = trail[y2][x2]
        if t2 == '#': continue
        elif t2 == '>':
            assert y2==y
            if x2 < x: continue
        elif t2 == '<':
            assert y2==y
            if x2 > x: continue
        elif t2 == 'v':
            assert x2==x
            if y2 < y: continue
        elif t2 == '^':
            assert x2==x
            if y2 > y: continue

        if path[-1] == (y2, x2): contine
        if (y2, x2) in path: continue

        walk(trail, path + [(y2, x2)], y2, x2)

walk(trail, [(y, x)], y, x)
print(best)
