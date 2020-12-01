#!/usr/bin/python3

with open('1a.txt') as f:
    lines = set(map(int, f.readlines()))

print(lines)

for left in lines:
    for middle in lines:
        right = 2020 - left - middle
        if right in lines:
            print(left, middle, right, left*middle*right)
