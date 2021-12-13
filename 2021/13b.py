#!/usr/bin/python3

import re

max_x, max_y = 0, 0

with open('13.txt') as f:
    for line in f:
        if m := re.match('(\d+),(\d+)', line):
            x, y = int(m.group(1)), int(m.group(2))
            max_x = max(max_x, x)
            max_y = max(max_y, y)

paper = [['.' for x in range(max_x+1)] for y in range(max_y+1)]
instructions = []

with open('13.txt') as f:
    for line in f:
        if m := re.match('(\d+),(\d+)', line):
            x, y = int(m.group(1)), int(m.group(2))
            paper[y][x] = '#'

        if m := re.match('fold along (.)=(\d+)', line):
            instructions.append((m.group(1), int(m.group(2))))

#print(paper)
print(max_x, max_y)

# 0 1 2 3 4
# 0 1 2 3

def fold_x(paper, fx):
    assert(fx == len(paper[0]) // 2)
    paper2 = [['.' for x in range(fx)] for y in range(len(paper))]

    for y in range(len(paper)):
        for x in range(fx):
            lower = paper[y][x]
            upper = paper[y][len(paper[0]) - x - 1]
            paper2[y][x] = '#' if lower == '#' or upper == '#' else '.'

    return paper2

def fold_y(paper, fy):
    assert(fy == len(paper) // 2)
    paper2 = [['.' for x in range(len(paper[0]))] for y in range(fy)]

    for y in range(fy):
        for x in range(len(paper[0])):
            lower = paper[y][x]
            upper = paper[len(paper) - y - 1][x]
            paper2[y][x] = '#' if lower == '#' or upper == '#' else '.'

    return paper2

for instruction in instructions:
    if instruction[0] == 'x':
        paper = fold_x(paper, instruction[1])
    else:
        paper = fold_y(paper, instruction[1])

for line in paper:
    print("".join(line))
