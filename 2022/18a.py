#!/usr/bin/python3

droplets = set()

with open("18.txt") as f:
    for line in f:
        droplet = tuple([int(x) for x in line.split(',')])
        droplets.add(droplet)

surface = 0

for droplet in droplets:
    x, y, z = droplet
    for n in [(x-1, y, z),
              (x+1, y, z),
              (x, y-1, z),
              (x, y+1, z),
              (x, y, z-1),
              (x, y, z+1)]:
        if n not in droplets:
            surface += 1

print(surface)
