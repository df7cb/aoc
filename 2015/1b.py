#!/usr/bin/python3

floor = 0
pos = 0

with open('1.txt') as f:
    for char in f.read():
        pos += 1
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

        if floor < 0:
            print('Entered basement at pos', pos)
            exit(0)
