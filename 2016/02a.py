#!/usr/bin/python3

def chew(line):
    x, y = 1, 1
    for char in line:
        if char == 'U':
            y -= 1
        elif char == 'D':
            y += 1
        elif char == 'L':
            x -= 1
        elif char == 'R':
            x += 1

        if x < 0:
            x = 0
        elif x > 2:
            x = 2
        if y < 0:
            y = 0
        elif y > 2:
            y = 2

    key = x + 3*y + 1
    print(key)

with open('02.txt') as f:
    for line in f:
        chew(line)
