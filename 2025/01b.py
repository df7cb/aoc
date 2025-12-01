#!/usr/bin/python3

import re

pos = 50
zero = 0

with open("01.txt") as f:
    for line in f:
        m = re.match(r"([LR])(\d+)", line)
        d = -1 if m.group(1) == 'L' else 1
        n = int(m.group(2))
        if n >= 100:
            zero += n // 100
            n = n % 100
        if n > 0:
            pos += d * n
            if pos >= 100:
                zero += 1
            elif pos == 0:
                zero += 1
            elif pos < 0 and pos != - n:
                zero += 1
            pos = pos % 100
        print(line, pos, zero)

print(zero)
