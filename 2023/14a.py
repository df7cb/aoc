#!/usr/bin/python3

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

print(platform)

tilt_north(platform)

print(platform)

weight = 0

for y in range(len(platform)):
    for x in range(len(platform[0])):
        if platform[y][x] == 'O':
            weight += len(platform) - y

print(weight)
