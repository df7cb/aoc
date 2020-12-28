#!/usr/bin/python3

import re

ranges = []

with open('20.txt') as f:
    for line in f:
        m = re.match('(\d+)-(\d+)', line)
        ranges.append((int(m[1]), int(m[2])))

maxip = 0
oldmaxip = None

while oldmaxip != maxip:
    oldmaxip = maxip
    for a, b in ranges:
        if a-1 <= maxip <= b:
            maxip = b

print('blocked:', 0, maxip)
print('20a:', maxip+1)
