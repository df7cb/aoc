#!/usr/bin/python3

import re

points = 0

with open("04.txt") as f:
    for line in f:
        m = re.match('Card *(\d+): (.*) \| (.*)', line)
        a = set(m.group(2).split())
        b = set(m.group(3).split())
        c = a.intersection(b)

        if len(c) > 0:
            points += 2 ** (len(c)-1)

        print(a, b, c, points)

print(points)
