#!/usr/bin/python3

import re

y, x, l = 0, 0, 0
polygon = [(y, x)]

def move(d, n):
    global y, x, l
    if d == 0:
        x += n
    elif d == 1:
        y += n
    elif d == 2:
        x -= n
    elif d == 3:
        y -= n
    else:
        assert 0
    #print(y, x)
    polygon.append((y, x))
    l += n

with open("18.txt") as f:
    for line in f:
        m = re.match('[RDLU] \d+ \(#([0-9a-f]{5})([0-3])\)', line)
        n = int(m.group(1), 0x10)
        d = int(m.group(2))
        move(d, n)

# https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon/451482#451482
def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p[:-1], p[1:])

print(area(polygon) + l/2 + 1)
