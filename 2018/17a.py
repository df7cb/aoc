#!/usr/bin/python3

import re
import sys
sys.setrecursionlimit(10000)

#x=560, y=1729..1742
#y=1288, x=483..485

range_x, range_y = 0, 0

with open('17.txt') as f:
    for line in f:
        if m := re.match('x=(\d+), y=(\d+)\.\.(\d+)', line):
            range_x = max(range_x, int(m.group(1)) + 1)
            range_y = max(range_y, int(m.group(3)) + 1)
        elif m := re.match('y=(\d+), x=(\d+)\.\.(\d+)', line):
            range_x = max(range_x, int(m.group(3)) + 1)
            range_y = max(range_y, int(m.group(1)) + 1)

ground = [list('.' * range_x) for y in range(range_y+1)]

with open('17.txt') as f:
    for line in f:
        if m := re.match('x=(\d+), y=(\d+)\.\.(\d+)', line):
            x = int(m.group(1))
            for y in range(int(m.group(2)), int(m.group(3))+1):
                ground[y][x] = '#'
        elif m := re.match('y=(\d+), x=(\d+)\.\.(\d+)', line):
            y = int(m.group(1))
            for x in range(int(m.group(2)), int(m.group(3))+1):
                ground[y][x] = '#'

ground[0][500] = '+'

#for line in ground:
#    print(''.join(line))

def flow(ground, y, x):
    area, blocked = 0, False
    if y == range_y - 1:
        return area, blocked
    # we've reached something down us blocking the flow
    if y < range_y-1 and ground[y+1][x] in ('#', '~', 'l', 'r', '|'):
        blocked = True
    # flow down if spot is free
    if y < range_y-1 and ground[y+1][x] == '.':
        ground[y+1][x] = '|'
        a2, blocked = flow(ground, y+1, x)
        area += 1 + a2
    # flow sidewards if something is blocking us
    if y < range_y-1 and blocked: # or ground[y+1][x] not in ('.', '~', '|')):
        #ground[y][x] = '~'
        #blocked = ground[y][x-1] not in ('.', '|', 'l', 'r') and ground[y][x+1] not in ('.', '|', 'l', 'r')

        bl = True
        xl = x-1
        while ground[y][xl] == '.':
            ground[y][xl] = 'l'
            area += 1
            if ground[y+1][xl] == '.':
                ground[y+1][xl] = '|'
                a2, bl = flow(ground, y+1, xl)
                area += 1 + a2
                if not bl:
                    break
            xl -= 1

        br = True
        xr = x+1
        while ground[y][xr] == '.':
            ground[y][xr] = 'r'
            area += 1
            if ground[y+1][xr] == '.':
                ground[y+1][xr] = '|'
                a2, br = flow(ground, y+1, xr)
                area += 1 + a2
                if not br:
                    break
            xr += 1

        blocked = bl and br
    return area, blocked

try:
    area, blocked = flow(ground, 0, 500)
    print(area, blocked)
except:
    pass

for line in ground:
    print(''.join(line))
