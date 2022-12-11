#!/usr/bin/python3

import re

wires = []

with open("03.txt") as f:
    for line in f:
        wires.append(line.strip().split(','))

grid = set()

x, y = 0, 0
for step in wires[0]:
    m = re.match('([UDLR])(\d+)', step)
    d, n = m.groups()
    if d == 'U':
        dx, dy = 0, -1
    elif d == 'D':
        dx, dy = 0, 1
    elif d == 'L':
        dx, dy = -1, 0
    elif d == 'R':
        dx, dy = 1, 0
    for i in range(int(n)):
        x += dx
        y += dy
        grid.add((x, y))

intersections = set()

x, y = 0, 0
for step in wires[1]:
    m = re.match('([UDLR])(\d+)', step)
    d, n = m.groups()
    if d == 'U':
        dx, dy = 0, -1
    elif d == 'D':
        dx, dy = 0, 1
    elif d == 'L':
        dx, dy = -1, 0
    elif d == 'R':
        dx, dy = 1, 0
    for i in range(int(n)):
        x += dx
        y += dy
        if (x, y) in grid:
            intersections.add((x, y))

print(intersections)

print(min({abs(x)+abs(y) for (x, y) in intersections}))
