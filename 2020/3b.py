#!/usr/bin/python3

with open('3.txt') as f:
    trees = f.readlines()

width = len(trees[0]) - 1 # chop newline
height = len(trees)

def slope(dx, dy):
    x, y = 0, 0
    number = 0

    while y < height:
        tree = trees[y][x % width]
        #print(y, x, tree)
        if tree == '#':
            number += 1
        x += dx
        y += dy

    return number

result = 1
for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    s = slope(dx, dy)
    print(s)
    result *= s

print(result)
