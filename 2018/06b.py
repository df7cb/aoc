#!/usr/bin/python3

import re

points = []

with open('06.txt') as f:
    for line in f:
        m = re.match('(\d+), (\d+)', line)
        points.append((int(m[1]), int(m[2])))

min_x = min(x[0] for x in points)
max_x = max(x[0] for x in points)
min_y = min(x[1] for x in points)
max_y = max(x[1] for x in points)

region_points = 0

for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        cum_dist = 0
        for p in points:
            dist = abs(x - p[0]) + abs(y - p[1])
            cum_dist += dist
        if cum_dist < 10000:
            region_points += 1

print('06b:', region_points)
