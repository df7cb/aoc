#!/usr/bin/python3

with open("21.txt") as f:
    garden = [line.strip() for line in f]

for y in range(len(garden)):
    if 'S' in garden[y]:
        x = garden[y].index('S')
        break

spots = set([(y, x)])
print(spots)

def print_garden(garden, spots):
    for y in range(len(garden)):
        for x in range(len(garden[0])):
            if (y, x) in spots: print('O', end='')
            else: print(garden[y][x], end='')
        print()

def move(spots):
    spots2 = set()

    for y, x in spots:
        for y2, x2 in ((y, x-1), (y, x+1), (y-1, x), (y+1, x)):
            if x2 >= 0 and x2 < len(garden[0]) and y2 >= 0 and y2 < len(garden):
                if garden[y2][x2] in ('.', 'S'):
                    spots2.add((y2, x2))

    return spots2

print_garden(garden, spots)

for i in range(64):
    spots = move(spots)
    print_garden(garden, spots)
    print(i+1, len(spots))
