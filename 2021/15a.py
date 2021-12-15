#!/usr/bin/python3

from collections import deque

with open('15.txt') as f:
    cavern = [[int(x) for x in line.strip()] for line in f]

def check(cavern, queue, dist, cost_here, x, y):
    if (x, y) not in dist or cost_here + cavern[y][x] < dist[(x, y)]:
        dist[(x, y)] = cost_here + cavern[y][x]
        queue.append((x, y))

def dijkstra(cavern):
    queue = deque([(0, 0)])
    dist = { (0, 0): 0 }

    while len(queue) > 0:
        x, y = queue.popleft()
        if x > 0:
            check(cavern, queue, dist, dist[(x, y)], x-1, y)
        if x < len(cavern[0]) - 1:
            check(cavern, queue, dist, dist[(x, y)], x+1, y)
        if y > 0:
            check(cavern, queue, dist, dist[(x, y)], x, y-1)
        if y < len(cavern) - 1:
            check(cavern, queue, dist, dist[(x, y)], x, y+1)

    return dist

dist = dijkstra(cavern)

print(dist[(len(cavern)-1, len(cavern[0])-1)])
