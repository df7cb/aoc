#!/usr/bin/python3

from collections import deque
from itertools import permutations

maze = []

with open('24.txt') as f:
    for line in f:
        maze.append(list(line.strip()))

start = {}
for y0 in range(len(maze)):
    for c in [str(x) for x in range(10)]:
        if c in maze[y0]:
            start[c] = (maze[y0].index(c), y0)

print(maze)
print(start)

distance = {}

def bfs(start, item):
    queue = deque([(start, 0, (0, 0))]) # maze with current track, current position, distance so far, items so far, last item found
    seen = set(start)
    while len(queue) > 0:
        (x, y), dist, (dx, dy) = queue.popleft()
        current = maze[y][x]
        if current != '.':
            print(f"Found {current} at {x},{y} distance {dist}")
            distance[item, current] = dist
            if len(distance) == 8: break
        for dx1, dy1 in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (dx1, dy1) == (-dx, -dy): continue
            x1, y1 = x+dx1, y+dy1
            if maze[y1][x1] == '#': continue
            if (x1, y1) in seen: continue
            queue.append(((x1,y1), dist+1, (dx1, dy1)))
            seen.add((x1, y1))

for item in start:
    bfs(start[item], item)

print(distance)

bestlen = 100000000
for path in permutations([x for x in start if x != '0']):
    path0 = ['0'] + list(path)
    length = 0
    for p in range(len(path0)-1):
        length += distance[path0[p], path0[p+1]]
    if length <= bestlen:
        bestlen = length
        print('24a:', path0, length)

bestlen = 100000000
for path in permutations([x for x in start if x != '0']):
    path0 = ['0'] + list(path) + ['0']
    length = 0
    for p in range(len(path0)-1):
        length += distance[path0[p], path0[p+1]]
    if length <= bestlen:
        bestlen = length
        print('24b:', path0, length)
