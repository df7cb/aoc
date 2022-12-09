#!/usr/bin/python3

import re

hx, hy = 0, 0
tx, ty = 0, 0

visited = set([(tx, ty)])

print(hx, hy, tx, ty)

with open("09.txt") as f:
    for line in f:
        m = re.match('([UDRL]) (\d+)', line)

        d, n = m.groups()
        print(d, n)

        if d == 'U':
            dx, dy = 0, -1
        elif d == 'D':
            dx, dy = 0, 1
        elif d == 'L':
            dx, dy = -1, 0
        elif d == 'R':
            dx, dy = 1, 0

        for step in range(int(n)):
            hx += dx
            hy += dy

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

            print(hx, hy, tx, ty)
            visited.add((tx, ty))

print(visited)
print(len(visited))
