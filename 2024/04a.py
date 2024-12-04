#!/usr/bin/python3

grid = []

with open("04.txt") as f:
    for line in f:
        grid.append(line.strip())

count = 0

def check(y, x):
    global count

    if grid[y][x] != 'X':
        return
    for dy in (-1, 0, 1):
        if y + 3*dy < 0: continue
        if y + 3*dy >= len(grid): continue
        for dx in (-1, 0, 1):
            if x + 3*dx < 0: continue
            if x + 3*dx >= len(grid[0]): continue
            if grid[y+dy][x+dx] != 'M': continue
            if grid[y+2*dy][x+2*dx] != 'A': continue
            if grid[y+3*dy][x+3*dx] != 'S': continue
            print(y, x, dy, dx)
            count += 1

for y in range(len(grid)):
    for x in range(len(grid[0])):
        check(y, x)

print(count)
