#!/usr/bin/python3

import re

vents = []

with open('05.txt') as f:
    for line in f:
        m = re.match('(\d+),(\d+) -> (\d+),(\d+)', line)
        ints = [int(i) for i in m.groups()]
        vents.append(ints)

floor = {}

for vent in vents:
    if vent[0] == vent[2]:
        yy = sorted([vent[1], vent[3]])
        for y in range(yy[0], yy[1]+1):
            p = (vent[0], y)
            if not p in floor:
                floor[p] = 0
            floor[p] += 1
    elif vent[1] == vent[3]:
        xx = sorted([vent[0], vent[2]])
        for x in range(xx[0], xx[1]+1):
            p = (x, vent[1])
            if not p in floor:
                floor[p] = 0
            floor[p] += 1

dangerous = len([p for p in floor if floor[p] > 1])

print("Dangerous points:", dangerous)
