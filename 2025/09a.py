#!/usr/bin/python3

tiles = []

with open("09.txt") as f:
    for line in f:
        tiles.append([int(x) for x in line.split(',')])

print(tiles)

def area(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

amax = 0
for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
        a = area(tiles[i], tiles[j])
        print(i, j, a)
        if a > amax:
            amax = a

print(amax)
