#!/usr/bin/python3

count = 0
good = 0

triangles = []

with open('03.txt') as f:
    for line in f:
        triangle = [int(x) for x in line.split()]
        triangles.append(triangle)

for y in range(0, len(triangles), 3):
    for x in range(3):
        triangle = [triangles[y][x], triangles[y+1][x], triangles[y+2][x]]
        triangle.sort()
        if sum(triangle[0:2]) > triangle[2]:
            good += 1
        count += 1

print(good, count)
