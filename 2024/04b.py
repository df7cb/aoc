#!/usr/bin/python3

grid = []

with open("04.txt") as f:
    for line in f:
        grid.append(line.strip())

count = 0

def check(y, x):
    if grid[y][x] != 'A':
        return 0

    if set([grid[y-1][x-1], grid[y+1][x+1]]) != set(['M', 'S']): return 0
    if set([grid[y-1][x+1], grid[y+1][x-1]]) != set(['M', 'S']): return 0

    return 1

for y in range(1, len(grid)-1):
    for x in range(len(grid[0])-1):
        count += check(y, x)

print(count)
