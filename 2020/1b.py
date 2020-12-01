#!/usr/bin/python3

with open('1a.txt') as f:
    lines = set(map(int, f.readlines()))

print(lines)

for left in lines:
    for middle in lines:
        for right in lines:
            if left + middle+ right == 2020:
                print(left, middle, right, left*middle*right)
