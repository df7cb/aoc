#!/usr/bin/python3

with open('25.txt') as f:
    sea = [list(line.strip()) for line in f]

width = len(sea[0])
height = len(sea)

def step(sea):
    moved = False

    sea2 = [['.' for x in line] for line in sea]
    for y in range(height):
        for x in range(width):
            if sea[y][x] == '>':
                if sea[y][(x+1)%width] == '.':
                    sea2[y][(x+1)%width] = '>'
                    moved = True
                else:
                    sea2[y][x] = '>'
            elif sea[y][x] == 'v':
                sea2[y][x] = 'v'

    sea3 = [['.' for x in line] for line in sea]
    for y in range(height):
        for x in range(width):
            if sea2[y][x] == 'v':
                if sea2[(y+1)%height][x] == '.':
                    sea3[(y+1)%height][x] = 'v'
                    moved = True
                else:
                    sea3[y][x] = 'v'
            elif sea2[y][x] == '>':
                sea3[y][x] = '>'

    return sea3, moved

moved = True
i = 0
while moved:
    print(i)
    for line in sea:
        print("".join(line))

    sea, moved = step(sea)
    i += 1

print(i)
for line in sea:
    print("".join(line))
