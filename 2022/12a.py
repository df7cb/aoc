#!/usr/bin/python3

from collections import deque

with open("12.txt") as f:
    grid = [line.strip() for line in f]

start = [x for x in range(len(grid)) if grid[x][0] == 'S'][0]
assert start >= 0

print(grid)

pos = (start, 0)
queue = deque([pos])
visited = {pos: 0}

while len(queue) > 0:
    pos = queue.popleft()
    print(pos)
