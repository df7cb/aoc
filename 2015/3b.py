#!/usr/bin/python3

map = {"0,0": True}
x, y = [0, 0], [0, 0]

houses = 1 # 0,0
r = 0 # 0 = santa, 1 = robo-santa

with open('3.txt') as f:
    for direction in f.read():
        if direction == '>':
            x[r] += 1
        elif direction == '<':
            x[r] -= 1
        elif direction == '^':
            y[r] += 1
        elif direction == 'v':
            y[r] -= 1
        if f'{x[r]},{y[r]}' not in map:
            houses += 1
            map[f'{x[r]},{y[r]}'] = True
        if r == 0:
            r = 1
        else:
            r = 0

print(houses)
