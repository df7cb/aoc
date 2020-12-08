#!/usr/bin/python3

floor = 0

with open('1.txt') as f:
    for char in f.read():
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

print(floor)
