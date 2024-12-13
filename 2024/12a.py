#!/usr/bin/python3

with open("12.txt") as f:
    garden = ['.' + line.strip() + '.' for line in f]
garden = ['.' * len(garden[0])] + garden + ['.' * len(garden[0])]

def walk(y, x, plant, visited):
    visited.add((y, x))
    a, u = 1, 0
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if garden[y+dy][x+dx] == plant and (y+dy, x+dx) not in visited:
            da, du = walk(y+dy, x+dx, plant, visited)
            a += da
            u += du
        elif garden[y+dy][x+dx] != plant:
            u += 1
    return a, u

cost = 0
visited = set()
for y in range(1, len(garden)-1):
    for x in range(1, len(garden[0])-1):
        if (y, x) not in visited:
            a, u = walk(y, x, garden[y][x], visited)
            price = a * u
            print(y, x, garden[y][x], a, u, price)
            cost += price

print(cost)
