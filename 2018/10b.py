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

def total_power(grid, s, x, y):
    total = 0
    for dx in range(s):
        for dy in range(s):
            total += grid[x+dx][y+dy]
    return total

def delta_power(grid, s, x, y, old):
    total = old
    for dy in range(s):
        total += grid[x+s-1][y+dy] - grid[x-1][y+dy]
    return total

best = 0

for s in range(1, 301):
    print("Size", s)
    for y in range(1, 302-s):
        t = total_power(grid, s, 1, y)
        for x in range(1, 302-s):
            if y > 1:
                t = delta_power(grid, s, x, y, t)
            if t >= best:
                best = t
                print(s, x, y, best)
