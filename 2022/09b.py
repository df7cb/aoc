#!/usr/bin/python3

import re

#rope = [(0, 0), (0, 0)]
rope = [(0, 0) for x in range(10)]

visited = set([rope[-1]])

#print(rope, visited)

with open("09.txt") as f:
    for line in f:
        m = re.match('([UDRL]) (\d+)', line)

        d, n = m.groups()
        #print(d, n)

        if d == 'U':
            dx, dy = 0, -1
        elif d == 'D':
            dx, dy = 0, 1
        elif d == 'L':
            dx, dy = -1, 0
        elif d == 'R':
            dx, dy = 1, 0

        for step in range(int(n)):
            hx, hy = rope[0]
            rope[0] = (hx+dx, hy+dy)

            for knot in range(1, len(rope)):
                hx, hy = rope[knot-1]
                tx, ty = rope[knot]

                if tx < hx-1:
                    if ty < hy:
                        ty += 1
                    elif ty > hy:
                        ty -= 1
                    tx += 1
                elif tx > hx+1:
                    if ty < hy:
                        ty += 1
                    elif ty > hy:
                        ty -= 1
                    tx -= 1
                elif ty < hy-1:
                    if tx < hx:
                        tx += 1
                    elif tx > hx:
                        tx -= 1
                    ty += 1
                elif ty > hy+1:
                    if tx < hx:
                        tx += 1
                    elif tx > hx:
                        tx -= 1
                    ty -= 1

                rope[knot] = (tx, ty)

                #print(rope)
            tail = rope[-1]
            visited.add(tail)

#print(visited)
print(len(visited))
