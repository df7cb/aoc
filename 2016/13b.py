#!/usr/bin/python3

from collections import deque

#input = 10
input = 1358

x0, y0 = 1, 1

seen = {(x0,y0)}
queue = deque([(0, x0,y0)]) # round number, x, y

def is_open(x, y):
    num = x*x + 3*x + 2*x*y + y + y*y + input
    ones = len([x for x in bin(num) if x == '1'])
    return ones % 2 == 0

while len(queue) > 0:
    r, x, y = queue.popleft()
    if r == 50: # stop here, all round-50 locations are already in "seen"
        break
    print(r, x, y)
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if x+dx < 0 or y+dy < 0:
            continue
        if (x+dx, y+dy) in seen:
            continue
        if not is_open(x+dx, y+dy):
            continue

        seen.add((x+dx, y+dy))
        queue.append((r+1, x+dx, y+dy))

print('13b:', len(seen))
