#!/usr/bin/python3

import euclide
import functools
import re

discs = []

with open('15.txt') as f:
    for line in f:
        m = re.match('Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', line)
        discs.append((int(m[2]), int(m[3]) + int(m[1])))

period, phase = functools.reduce(lambda a, b: euclide.combine_phased_rotations(a[0], a[1], b[0], b[1]), discs)

print(period, phase, '15a:', period-phase)

# 15b:
discs.append((11, 0 + len(discs)+1))

period, phase = functools.reduce(lambda a, b: euclide.combine_phased_rotations(a[0], a[1], b[0], b[1]), discs)

print(period, phase, '15b:', period-phase)
