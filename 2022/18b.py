#!/usr/bin/python3

from collections import deque

droplets = set()

with open("18.txt") as f:
    for line in f:
        droplet = tuple([int(x) for x in line.split(',')])
        droplets.add(droplet)

min_x = min({x[0] for x in droplets})-1
max_x = max({x[0] for x in droplets})+1
min_y = min({x[1] for x in droplets})-1
max_y = max({x[1] for x in droplets})+1
min_z = min({x[2] for x in droplets})-1
max_z = max({x[2] for x in droplets})+1

start = (min_x, min_y, min_z)
assert start not in droplets
exterior = {start}

queue = deque([start])
while queue:
    x, y, z = queue.popleft()
    for n in [(x-1, y, z),
              (x+1, y, z),
              (x, y-1, z),
              (x, y+1, z),
              (x, y, z-1),
              (x, y, z+1)]:
        nx, ny, nz = n
        if nx < min_x or nx > max_x or ny < min_y or ny > max_y or nz < min_z or nz > max_z:
            continue
        if n not in exterior and n not in droplets:
            exterior.add(n)
            queue.append(n)

surface = 0

for droplet in droplets:
    x, y, z = droplet
    for n in [(x-1, y, z),
              (x+1, y, z),
              (x, y-1, z),
              (x, y+1, z),
              (x, y, z-1),
              (x, y, z+1)]:
        if n in exterior and n not in droplets:
            surface += 1

print(surface)
