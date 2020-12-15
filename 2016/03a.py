#!/usr/bin/python3

count = 0
good = 0

with open('03.txt') as f:
    for line in f:
        triangle = [int(x) for x in line.split()]
        triangle.sort()

        if sum(triangle[0:2]) > triangle[2]:
            good += 1
        count += 1

print(good, count)
