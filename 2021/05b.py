#!/usr/bin/python3

import re
from numpy import sign

vents = []

with open('05.txt') as f:
    for line in f:
        m = re.match('(\d+),(\d+) -> (\d+),(\d+)', line)
        ints = [int(i) for i in m.groups()]
        vents.append(ints)

floor = {}

for vent in vents:
    p = (vent[0], vent[1])
    dp = (sign(vent[2] - vent[0]), sign(vent[3] - vent[1]))
    while True:
        if not p in floor:
            floor[p] = 0
        floor[p] += 1
        if p == (vent[2], vent[3]):
            break
        p = (p[0] + dp[0], p[1] + dp[1])

dangerous = len([p for p in floor if floor[p] > 1])

print("Dangerous points:", dangerous)
