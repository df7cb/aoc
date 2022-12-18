#!/usr/bin/python3

from copy import deepcopy

with open("17.txt") as f:
    wind = f.read().strip()

rocks = [
        ['####'],
        [' # ',
         '###',
         ' # '],
        ['###', # rocks fall up here
         '  #',
         '  #'],
        ['#',
         '#',
         '#',
         '#'],
        ['##',
         '##']
        ]

chamber = [
        list('.......'),
        list('.......'),
        list('.......'),
        ]

def collision(chamber, rock, y, x):
    if x < 0 or x > 7 - len(rock[0]):
        return True
    if y < 0:
        return True
    for row in range(len(rock)):
        if y+row >= len(chamber):
            continue
        for col in range(len(rock[0])):
            if rock[row][col] == '#':
                if chamber[y+row][x+col] == '#':
                    return True
    return False

def place_rock(chamber, rock, y, x):
    for row in range(len(rock)):
        if y+row >= len(chamber):
            chamber.append(list('.......'))
        for col in range(len(rock[0])):
            if rock[row][col] == '#':
                chamber[y+row][x+col] = '#'

def print_chamber(chamber):
    for row in chamber:
        print(''.join(row))
    print()

rockcount = 0
windcount = 0
start_y = 3

def run(steps):
    global rockcount
    global windcount
    global start_y

    for step in range(steps):
        rock = rocks[rockcount % len(rocks)]
        rockcount += 1

        while chamber[start_y - 3] != list('.......'):
            chamber.append(list('.......'))
            start_y += 1

        y = start_y
        x = 2

        while True:
            # wind
            winddir = -1 if wind[windcount % len(wind)] == '<' else 1
            #print(y, x, winddir)
            windcount += 1
            if not collision(chamber, rock, y, x+winddir):
                x += winddir
            #chamber2 = deepcopy(chamber)
            #place_rock(chamber2, rock, y, x)
            #print_chamber(chamber2)

            # fall
            if not collision(chamber, rock, y-1, x):
                y -= 1
            else:
                break
            #chamber2 = deepcopy(chamber)
            #place_rock(chamber2, rock, y, x)
            #print_chamber(chamber2)

        place_rock(chamber, rock, y, x)
        #print_chamber(chamber)

    while chamber[start_y - 3] != list('.......'):
        chamber.append(list('.......'))
        start_y += 1

run(2022)

print_chamber(chamber)
print("height", start_y-3)
