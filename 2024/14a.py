#!/usr/bin/python3

import re

sx = 101 # 11
sy = 103 # 7

robots = []

with open("14.txt") as f:
    for line in f:
        m = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
        robots.append([int(x) for x in m.groups()])
        assert robots[-1][0] < sx
        assert robots[-1][1] < sy

print(robots)

for r in robots:
    r[0], r[1] = (r[0] + 100*r[2]) % sx, (r[1] + 100*r[3]) % sy

print(robots)

quadrants = [[0, 0], [0, 0]]

for r in robots:
    if r[0] < (sx-1)/2 and r[1] < (sy-1)/2:
        quadrants[0][0] += 1
    elif r[0] > (sx-1)/2 and r[1] < (sy-1)/2:
        quadrants[1][0] += 1
    elif r[0] < (sx-1)/2 and r[1] > (sy-1)/2:
        quadrants[0][1] += 1
    elif r[0] > (sx-1)/2 and r[1] > (sy-1)/2:
        quadrants[1][1] += 1

print(quadrants)
print(quadrants[0][0] * quadrants[1][0] * quadrants[0][1] * quadrants[1][1])
