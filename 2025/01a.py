#!/usr/bin/python3

import re

pos = 50
zero = 0

with open("01.txt") as f:
    for line in f:
        m = re.match(r"([LR])(\d+)", line)
        d = -1 if m.group(1) == 'L' else 1
        n = int(m.group(2))
        pos = (pos + d * n) % 100
        if pos == 0:
            zero += 1
        print(pos)

print(zero)
