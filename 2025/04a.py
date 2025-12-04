#!/usr/bin/python3

with open("04.txt") as f:
    grid = [list(line.strip()) for line in f]

for line in grid:
    print(line)

print()

lift_rolls = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '.': continue
        rolls = 0
        for dy in (-1, 0, 1):
            if y + dy < 0 or y + dy >= len(grid): continue
            for dx in (-1, 0, 1):
                if (dy, dx) == (0, 0): continue
                if x + dx < 0 or x + dx >= len(grid[0]): continue
                if grid[y+dy][x+dx] != '.':
                    rolls += 1

        if rolls < 4:
            if grid[y][x] == '@':
                grid[y][x] = 'x'
                lift_rolls += 1

for line in grid:
    print(line)

print(lift_rolls)
