#!/usr/bin/python3

import sys
sys.setrecursionlimit(1000000)

y, x = 0, 0
hole = set([(y, x)])

def move(d, n):
    global y, x
    for i in range(n):
        if d == 'U':
            y -= 1
        elif d == 'D':
            y += 1
        elif d == 'L':
            x -= 1
        elif d == 'R':
            x += 1
        else:
            assert 0
        print(y, x)
        hole.add((y, x))

with open("18.txt") as f:
    for line in f:
        d, n, color = line.split()
        move(d, 2*int(n))

miny = min([h[0] for h in hole])
maxy = max([h[0] for h in hole])
minx = min([h[1] for h in hole])
maxx = max([h[1] for h in hole])

for y in range(miny, maxy+1):
    for x in range(minx, maxx+1):
        print('#' if (y, x) in hole else '.', end='')
    print()

def fill(hole, y, x):
    while (y, x) not in hole:
        hole.add((y, x))
        for y1, x1 in ((y, x-1), (y-1, x), (y+1, x)):
            if (y1, x1) not in hole:
                fill(hole, y1, x1)
        x+=1

fill(hole, 1, 1) # guess interrior

for y in range(miny, maxy+1):
    for x in range(minx, maxx+1):
        print('#' if (y, x) in hole else '.', end='')
    print()

count = 0
for y in range(miny, maxy+1, 2):
    for x in range(minx, maxx+1, 2):
        if (y, x) in hole:
            count += 1

print(count)
