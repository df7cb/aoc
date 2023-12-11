#!/usr/bin/python3

with open("11.txt") as f:
    space = [[c for c in line.strip()] for line in f]
    space2 = [[c for c in line] for line in space]

def print_space(space):
    for line in space:
        print(''.join(line))
    print()

#print_space(space2)

y2 = 0
for y in range(len(space)):
    if '#' not in space[y]:
        space2 = space2[:y2] + [space2[y2], space2[y2]] + space2[y2+1:]
        y2 += 1
        #print_space(space2)
    y2 += 1

space = [[c for c in line] for line in space2]

x2 = 0
for x in range(len(space[0])):
    if '#' not in [space[y][x] for y in range(len(space))]:
        for y in range(len(space)):
            space2[y] = space2[y][:x2] + [space2[y][x2], space2[y][x2]] + space2[y][x2+1:]
        x2 += 1
        #print_space(space2)
    x2 += 1

print_space(space2)

galaxies = []

for y in range(len(space2)):
    for x in range(len(space2[0])):
        if space2[y][x] == '#':
            galaxies.append((y, x))

def manhattan(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

print(galaxies)

dist = 0

for g1 in range(len(galaxies) - 1):
    for g2 in range(g1 + 1, len(galaxies)):
        print(g1, g2, manhattan(galaxies[g1], galaxies[g2]))
        dist += manhattan(galaxies[g1], galaxies[g2])

print(dist)
