#!/usr/bin/python3

import re

fabric = [[[] for x in range(1000)] for y in range(1000)]

claims = set()
double_claims = set()

with open('03.txt') as f:
    for line in f:
        m = re.match('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
        claim, x0, y0, w, h = int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])
        claims.add(claim)
        for y in range(y0, y0+h):
            for x in range(x0, x0+w):
                fabric[y][x].append(claim)
                if len(fabric[y][x]) > 1:
                    [double_claims.add(f) for f in fabric[y][x]]

print('03b:', claims - double_claims)
