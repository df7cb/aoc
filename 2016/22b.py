#!/usr/bin/python3

import re

grid = {}

with open('22.txt') as f:
    for line in f:
        if m := re.match('/dev/grid/node-x(\d+)-y(\d+) *(\d+)T *(\d+)T *(\d+)T', line):
            x, y = int(m[1]), int(m[2])
            used, avail = int(m[4]), int(m[5])
            grid[x,y] = {"used": used, "avail": avail}

print(grid)

max_x = max([g[0] for g in grid])
max_y = max([g[1] for g in grid])
print(max_x, max_y)

for y in range(max_y+1):
    for x in range(max_x+1):
        print(grid[x,y]["used"], end='  ')
    print()

print('22b:', 31 + 5*30)
