#!/usr/bin/python3

import re

grid = {}

with open('22.txt') as f:
    for line in f:
        if m := re.match('/dev/grid/node-x(\d+)-y(\d+) *(\d+)T *(\d+)T *(\d+)T', line):
            x, y = int(m[1]), int(m[2])
            size, used, avail = int(m[3]), int(m[4]), int(m[5])
            grid[x,y] = {"size": size, "used": used, "avail": avail}

print(grid)

viable = 0
for a in grid:
    for b in grid:
        if a!=b and grid[a]['used'] > 0 and grid[a]['used'] <= grid[b]['avail']:
            print(a, b)
            viable += 1

print(viable)
