#!/usr/bin/python3

with open('1a.txt') as f:
    lines = set(map(int, f.readlines()))

print(lines)

for left in lines:
    for right in lines:
        if left + right == 2020:
            print(left, right, left*right)
