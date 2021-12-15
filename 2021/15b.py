#!/usr/bin/python3

import heapq

with open('15.txt') as f:
    cavern = [[int(x) for x in line.strip()] for line in f]

def inc(x, i):
    x += i
    if x > 9:
        x -= 9
    return x

cavern5 = []
for yy in range(5):
    for line in cavern:
        line2 = []
        for xx in range(5):
            line2.extend([inc(x, xx+yy) for x in line])
        cavern5.append(line2)

def check(cavern, queue, dist, cost_here, x, y):
    cost_new = cost_here + cavern[y][x]
    if dist[y][x] < 0 or cost_new < dist[y][x]:
        dist[y][x] = cost_new
        heapq.heappush(queue, (cost_new, (x, y)))

def dijkstra(cavern, dist):
    queue = [(0, (0, 0))]
    heapq.heapify(queue)

    while len(queue) > 0:
        cost, (x, y) = heapq.heappop(queue)
        if x > 0:
            check(cavern, queue, dist, dist[y][x], x-1, y)
        if x < len(cavern[0]) - 1:
            check(cavern, queue, dist, dist[y][x], x+1, y)
        if y > 0:
            check(cavern, queue, dist, dist[y][x], x, y-1)
        if y < len(cavern) - 1:
            check(cavern, queue, dist, dist[y][x], x, y+1)

    return dist

dist = [[-1 for x in line] for line in cavern5]
dist[0][0] = 0
dist = dijkstra(cavern5, dist)

print(dist[len(cavern5)-1][len(cavern5[0])-1])
