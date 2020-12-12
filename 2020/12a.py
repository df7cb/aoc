#!/usr/bin/python3

import re

x, y = 0, 0
dirs = ['N', 'E', 'S', 'W']
d = 1

with open('12.txt') as f:
    for line in f:
        m = re.match('([NSEWFLR])(\d+)', line)
        c = m[1]
        i = int(m[2])

        if c == 'F':
            c = dirs[d]

        if c == 'N':
            y += i
        elif c == 'S':
            y -= i
        elif c == 'E':
            x += i
        elif c == 'W':
            x -= i
        elif c == 'R':
            d = int((d + i/90) % 4)
        elif c == 'L':
            d = int((d - i/90) % 4)

        print (line.strip(), x, y, dirs[d])

print(x, y, abs(x)+abs(y))
