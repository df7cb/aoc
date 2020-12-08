#!/usr/bin/python3

import re

wrapping = 0

with open('2.txt') as f:
    for box in f:
        m = re.match('(\d+)x(\d+)x(\d+)', box)
        l, w, h = int(m.group(1)), int(m.group(2)), int(m.group(3))

        l1, l2 = sorted([l, w, h])[0:2] # smallest side area

        print(l, w, h, 2*l*w + 2*w*h + 2*h*l, l1*l2)
        wrapping += 2*l*w + 2*w*h + 2*h*l + l1*l2

print(wrapping)
