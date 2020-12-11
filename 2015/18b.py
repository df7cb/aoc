#!/usr/bin/python3

grid = []
size = 100

with open('18.txt') as f:
    for line in f:
        grid.append(list(line))

def neighbors(grid, y, x):
    n = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            if x + dx < 0 or x + dx >= 100:
                continue
            if y + dy < 0 or y + dy >= 100:
                continue
            if grid[y+dy][x+dx] == '#':
                n += 1
    return n

def stuck(grid):
    grid[0][0] = '#'
    grid[0][99] = '#'
    grid[99][0] = '#'
    grid[99][99] = '#'

def update(grid):
    newgrid = []
    updated = False
    for y in range(100):
        newgrid.append([])
        for x in range(100):
            n = neighbors(grid, y, x)
            if grid[y][x] == '#' and n < 2 or n > 3:
                newgrid[y].append('.')
                updated = True
            elif grid[y][x] == '.' and n == 3:
                newgrid[y].append('#')
                updated = True
            else:
                newgrid[y].append(grid[y][x])
    return updated, newgrid

updated = True
stuck(grid)
for x in range(100):
    updated, grid = update(grid)
    stuck(grid)
    print(grid)

count = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == '#':
            count += 1
print(count)

