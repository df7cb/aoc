#!/usr/bin/python3

import re

fabric = [[0 for x in range(1000)] for y in range(1000)]

with open('03.txt') as f:
    for line in f:
        m = re.match('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
        x0, y0, w, h = int(m[2]), int(m[3]), int(m[4]), int(m[5])
        for y in range(y0, y0+h):
            for x in range(x0, x0+w):
                fabric[y][x] += 1

double = 0
for y in range(0, 1000):
    for x in range(0, 1000):
        if fabric[y][x] > 1:
            double += 1

print('03a:', double)
