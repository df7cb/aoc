#!/usr/bin/python3

from copy import deepcopy

with open("14.txt") as f:
    platform = [list(line.strip()) for line in f]

def tilt_north(platform):
    for y in range(len(platform)):
        for x in range(len(platform[0])):
            if platform[y][x] == 'O':
                y2 = y
                while y2 > 0 and platform[y2-1][x] == '.':
                    platform[y2][x] = '.'
                    platform[y2-1][x] = 'O'
                    y2 -= 1

def tilt_west(platform):
    for x in range(len(platform[0])):
        for y in range(len(platform)):
            if platform[y][x] == 'O':
                x2 = x
                while x2 > 0 and platform[y][x2-1] == '.':
                    platform[y][x2] = '.'
                    platform[y][x2-1] = 'O'
                    x2 -= 1

def tilt_south(platform):
    for y in range(len(platform)-1, -1, -1):
        for x in range(len(platform[0])):
            if platform[y][x] == 'O':
                y2 = y
                while y2 < len(platform)-1 and platform[y2+1][x] == '.':
                    platform[y2][x] = '.'
                    platform[y2+1][x] = 'O'
                    y2 += 1

def tilt_east(platform):
    for x in range(len(platform[0])-1, -1, -1):
        for y in range(len(platform)):
            if platform[y][x] == 'O':
                x2 = x
                while x2 < len(platform[0])-1 and platform[y][x2+1] == '.':
                    platform[y][x2] = '.'
                    platform[y][x2+1] = 'O'
                    x2 += 1

def print_platform(platform):
    for line in platform:
        print(''.join(line))

def spin(platform):
    tilt_north(platform)
    tilt_west(platform)
    tilt_south(platform)
    tilt_east(platform)

def load(platform):
    weight = 0
    for y in range(len(platform)):
        for x in range(len(platform[0])):
            if platform[y][x] == 'O':
                weight += len(platform) - y
    return weight

count = 0
oldplatform = []
while count != 1000000000:
    spin(platform)
    count += 1
    print(count)
    print_platform(platform)
    print(load(platform))
    print()
    if platform in oldplatform:
        last = oldplatform.index(platform)
        cycle = len(oldplatform) - last
        print(len(oldplatform), last, "cycle")
        count += ((1000000000 - count) // cycle) * cycle
    oldplatform.append(deepcopy(platform))

print(load(platform))
