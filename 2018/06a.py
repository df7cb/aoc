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

infinite_points = set()
labels = {}

for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        min_dist = 100000
        for p in points:
            dist = abs(x - p[0]) + abs(y - p[1])
            if dist < min_dist:
                min_point = [p]
                min_dist = dist
            elif dist == min_dist:
                min_point.append(p)
        if len(min_point) == 1:
            p = min_point[0]
            if x in (min_x, max_x) or y in (min_y, max_y):
                infinite_points.add(p)
            else:
                #print(x, y, p, min_dist)
                if p not in labels:
                    labels[p] = 0
                labels[p] += 1

print(labels)
largest_area = max(labels.values())
largest_point = [x for x in points if labels[x] == largest_area]
print('06a:', largest_point, largest_area)
