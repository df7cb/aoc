#!/usr/bin/python3

hubble = 1000000 - 1

with open("11.txt") as f:
    space = [[c for c in line.strip()] for line in f]

def print_space(space):
    for line in space:
        print(''.join(line))
    print()

empty_rows = [0 for y in range(len(space))]

for y in range(len(space)):
    if '#' not in space[y]:
        empty_rows[y] = hubble

empty_cols = [0 for x in range(len(space[0]))]

for x in range(len(space[0])):
    if '#' not in [space[y][x] for y in range(len(space))]:
        empty_cols[x] = hubble

galaxies = []

for y in range(len(space)):
    for x in range(len(space[0])):
        if space[y][x] == '#':
            galaxies.append((y, x))

def manhattan(g1, g2):
    g1y, g1x = g1
    g2y, g2x = g2
    return abs(g1y - g2y) + abs(g1x - g2x) + \
            sum(empty_rows[min(g1y, g2y):max(g1y, g2y)]) + \
            sum(empty_cols[min(g1x, g2x):max(g1x, g2x)])

print(galaxies)

dist = 0

for g1 in range(len(galaxies) - 1):
    for g2 in range(g1 + 1, len(galaxies)):
        #print(g1, g2, manhattan(galaxies[g1], galaxies[g2]))
        dist += manhattan(galaxies[g1], galaxies[g2])

print(dist)
