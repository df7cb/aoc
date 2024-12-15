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

def print_robots(robots):
    grid = [list('.' * sx) for y in range(sy)]
    for r in robots:
        grid[r[1]][r[0]] = '#'
    for line in grid:
        print(''.join(line))

print_robots(robots)

s = 0
while True:
    s+=1
    print(s)
    for r in robots:
        r[0], r[1] = (r[0] + r[2]) % sx, (r[1] + r[3]) % sy
    print_robots(robots)
    print()

    center = 0
    for r in robots:
        if sx/3 <= r[0] <= 2*sx/3 and \
           sy/3 <= r[1] <= 2*sy/3:
               center += 1

    if center > 150:
        print(center)
        break
