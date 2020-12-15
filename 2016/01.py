#!/usr/bin/python3

import re

instructions = 'R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, R1, R5, L1, L3, L5, R2'

x, y = 0, 0
dx, dy = 1, 0

seen = {}

for i in instructions.split(', '):
    m = re.match('([LR])(\d+)', i)
    if m[1] == 'L':
        dx, dy = -dy, dx
    else:
        dx, dy = dy, -dx
    for r in range(int(m[2])):
        x += dx
        y += dy
        #print(i, x, y, dx, dy)
        if (x, y) in seen:
            print(x, y, 'was seen before', abs(x)+abs(y))
        seen[x, y] = True

print(abs(x)+abs(y))
