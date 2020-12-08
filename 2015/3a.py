#!/usr/bin/python3

map = {"0,0": True}
x, y = 0, 0

houses = 1 # 0,0

with open('3.txt') as f:
    for direction in f.read():
        if direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        elif direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        if f'{x},{y}' not in map:
            houses += 1
            map[f'{x},{y}'] = True

print(houses)
