#!/usr/bin/python3

import re
from time import sleep

blocks = []

size_x, size_y = 6, 10 # 9356 solutions (with 291131199 steps)
#size_x, size_y = 5, 12 # 4040 solutions
#size_x, size_y = 4, 15 # 1472 solutions

with open('12blocks.txt') as f:
    block = []
    for line in f:
        if m := re.match('(\d+):', line):
            blocks.append([])
        elif line == '\n':
            assert block[0][0:4] == '   #'
            blocks[-1].append(block)
            block = []
        else:
            block.append(line.rstrip())

def dump(grid):
    for line in grid:
        for x in line:
            b = 40 + x // 2
            f = 37 - (x % 7)
            print(f"\033[{f};{b}m{x:2d}", end=' ')
        print('\033[0m')

solutions = 0
tries = 0

def try_block(grid, numbers, num, block, x, y):
    global tries
    tries += 1
    # check if block fits
    for by in range(len(block)):
        for bx in range(len(block[by])):
            if block[by][bx] == '#':
                if not (0 <= x + bx - 3 < size_x) or y + by >= size_y:
                    return # block outside grid
                if grid[y+by][x+bx-3] != -1:
                    return # block overlaps existing block

    # build new grid
    grid2 = [[x for x in g] for g in grid]
    for by in range(len(block)):
        for bx in range(len(block[by])):
            if block[by][bx] == '#':
                grid2[y+by][x+bx-3] = num
    assert grid2[y][x] == num

    #print()
    #dump(grid2)
    #sleep(0.001)

    numbers2 = {x for x in numbers if x != num}

    while y < size_y and grid2[y][x] != -1:
        x += 1
        if x >= size_x:
            x = 0
            y += 1

    if y < size_y:
        try_blocks(grid2, numbers2, x, y)
    else:
        global solutions
        solutions += 1
        print("Found solution", solutions, tries)
        dump(grid2)
        print()

def try_blocks(grid, numbers, x, y):
    for num in numbers:
        for block in blocks[num]:
            try_block(grid, numbers, num, block, x, y)

numbers = set(range(12))
grid = [[-1 for x in range(size_x)] for y in range(size_y)] # 6x10

try_blocks(grid, numbers, 0, 0)
