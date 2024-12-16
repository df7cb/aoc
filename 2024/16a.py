#!/usr/bin/python3

from collections import deque

with open("16.txt") as f:
    maze = f.readlines()

for y in range(len(maze)):
    if 'S' in maze[y]:
        x = maze[y].index('S')
        break

dy, dx = 0, 1

queue = deque([(y, x, dy, dx, 0)])
seen = {}
best = None

while queue:
    y, x, dy, dx, s = queue.popleft()
    if maze[y][x] == 'E':
        print(y, x, dy, dx, s)
        #exit(0)
        if best == None or s < best:
            best = s
    if (y, x, dy, dx) in seen and seen[(y, x, dy, dx)] <= s: continue
    seen[(y, x, dy, dx)] = s

    if maze[y+dy][x+dx] != '#':
        queue.append((y+dy, x+dx, dy, dx, s+1))
    queue.append((y, x, dx, -dy, s+1000))
    queue.append((y, x, -dx, dy, s+1000))

print(best)
