#!/usr/bin/python3

from collections import deque

corrupted = set()

with open("18.txt") as f:
    n = 0
    for line in f:
        x, y = [int(x) for x in line.split(',')]
        corrupted.add((x, y))
        n += 1
        if n == 1024: break

queue = deque([(0, 0, 0)])
seen = set()

while queue:
    x, y, d = queue.popleft()
    print(x, y, d)
    if (x, y) == (70, 70):
        print(d)
        break
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x2, y2 = x+dx, y+dy
        if 0 <= x2 < 71 and 0 <= y2 < 71 and not (x2, y2) in corrupted and not (x2, y2) in seen:
            seen.add((x2, y2))
            queue.append((x2, y2, d+1))
