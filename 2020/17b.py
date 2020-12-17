#!/usr/bin/python3

import re

grid = set()

with open('17.txt') as f:
    y = 0
    for line in f:
        for x in range(len(line.strip())):
            if line[x] == '#':
                grid.add((x, y, 0, 0))
        y += 1

def neighbors(grid, x, y, z, w):
    n = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                for dw in (-1, 0, 1):
                    if dx == dy == dz == dw == 0:
                        continue
                    if (x+dx, y+dy, z+dz, w+dw) in grid:
                        n += 1
    return n

def step(grid):
    min_x = min(c[0] for c in grid)
    max_x = max(c[0] for c in grid)
    min_y = min(c[1] for c in grid)
    max_y = max(c[1] for c in grid)
    min_z = min(c[2] for c in grid)
    max_z = max(c[2] for c in grid)
    min_w = min(c[3] for c in grid)
    max_w = max(c[3] for c in grid)
    grid2 = set()

    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            for z in range(min_z-1, max_z+2):
                for w in range(min_w-1, max_w+2):

                    n = neighbors(grid, x, y, z, w)
                    if (x, y, z, w) in grid and n in (2, 3):
                        grid2.add((x, y, z, w))
                    elif (x, y, z) not in grid and n == 3:
                        grid2.add((x, y, z, w))

    return grid2

def dump(grid):
    min_x = min(c[0] for c in grid)
    max_x = max(c[0] for c in grid)
    min_y = min(c[1] for c in grid)
    max_y = max(c[1] for c in grid)
    min_z = min(c[2] for c in grid)
    max_z = max(c[2] for c in grid)
    min_w = min(c[3] for c in grid)
    max_w = max(c[3] for c in grid)
    for y in range(min_y, max_y+1):
        for z in range(min_z, max_z+1):
            print(z, end=' ')
            for x in range(min_x, max_x+1):
                for w in range(min_w, max_w+1):
                    if (x, y, z, w) in grid:
                        print('#', end='')
                    else:
                        print('.', end='')
            print('  ', end='')
        print()
    print()

print(len(grid))
dump(grid)
for i in range(6):
    grid = step(grid)
    print(i, len(grid))
    #dump(grid)
