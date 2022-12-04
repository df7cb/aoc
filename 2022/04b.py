#!/usr/bin/python3

import re

total = 0

with open("04.txt") as f:
    for line in f:
        m = re.match('(\d+)-(\d+),(\d+)-(\d+)', line)
        a, b, x, y = [int(x) for x in m.groups()]
        assert a <= b
        assert x <= y

        if a > y or b < x:
            continue
        print(m.groups())
        total += 1

print(total)
