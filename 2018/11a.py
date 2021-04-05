#!/usr/bin/python3

input = 7347

def power(x, y):
    rack_id = x + 10
    p = rack_id * y
    p += input
    p *= rack_id
    p = (p // 100) % 10
    return p - 5

grid = [[power(x, y) for y in range(301)] for x in range(301)]

def total_power(grid, x, y):
    return grid[x+0][y+0] + \
           grid[x+1][y+0] + \
           grid[x+2][y+0] + \
           grid[x+0][y+1] + \
           grid[x+1][y+1] + \
           grid[x+2][y+1] + \
           grid[x+0][y+2] + \
           grid[x+1][y+2] + \
           grid[x+2][y+2]

best = 0

for x in range(1,299):
    for y in range(1,299):
        t = total_power(grid, x, y)
        if t >= best:
            best = t
            print(x, y, best)
