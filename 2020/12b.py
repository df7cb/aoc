#!/usr/bin/python3

import re

x, y = 0, 0
wx, wy = 10, 1

with open('12.txt') as f:
    for line in f:
        m = re.match('([NSEWFLR])(\d+)', line)
        c = m[1]
        i = int(m[2])

        if c == 'F':
            x += i * wx
            y += i * wy
        elif c == 'N':
            wy += i
        elif c == 'S':
            wy -= i
        elif c == 'E':
            wx += i
        elif c == 'W':
            wx -= i
        elif c == 'R':
            for r in range(0, int(i/90)):
                wx, wy = wy, -wx
        elif c == 'L':
            for r in range(0, int(i/90)):
                wx, wy = -wy, wx

        print (line.strip(), x, y, wx, wy)

print(x, y, abs(x)+abs(y))
