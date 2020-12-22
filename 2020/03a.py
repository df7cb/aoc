#!/usr/bin/python3

with open('03.txt') as f:
    trees = f.readlines()

print(''.join(trees))

width = len(trees[0]) - 1 # chop newline
height = len(trees)
print (width, height)

x, y = 0, 0
number = 0

while y < height:
    tree = trees[y][x % width]
    print(y, x, tree)
    if tree == '#':
        number += 1
    x += 3
    y += 1

print(number)
