#!/usr/bin/python3

import re

#x=560, y=1729..1742
#y=1288, x=483..485

range_x, range_y = 0, 0

with open('17.txt') as f:
    for line in f:
        if m := re.match('x=(\d+), y=(\d+)\.\.(\d+)', line):
            range_x = max(range_x, int(m.group(1)) + 2)
            range_y = max(range_y, int(m.group(3)) + 1)
        elif m := re.match('y=(\d+), x=(\d+)\.\.(\d+)', line):
            range_x = max(range_x, int(m.group(3)) + 2)
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
    area = 0

    # flow down until we reach ground
    yy = y + 1
    while ground[yy][x] == '.':
        area += 1
        ground[yy][x] = '|'
        yy += 1
        if yy == range_y:
            return area

    if ground[yy][x] == '|': # flowing water discovered, stop here
        return area

    while True:
        yy -= 1 # up one level (originally on the ground)
        #assert(ground[yy][x] in ('|', '~'))
        if ground[yy][x] == '.':
            area += 1
            ground[yy][x] = '|'

        # flow to the left
        xl = x - 1
        bl = False
        while ground[yy][xl] in ('.', '|', '~') and ground[yy+1][xl] not in ('.', '|'):
            if ground[yy][xl] == '.':
                area += 1
                ground[yy][xl] = '|'
            xl -= 1
        if ground[yy+1][xl] not in ('.', '|'): # no exit at this end
            bl = True
        else: # exit found
            if ground[yy][xl] == '.':
                area += 1
                ground[yy][xl] = '|'

        # flow to the right
        xr = x + 1
        br = False
        while ground[yy][xr] in ('.', '|', '~') and ground[yy+1][xr] not in ('.', '|'):
            if ground[yy][xr] == '.':
                area += 1
                ground[yy][xr] = '|'
            xr += 1
            if xr >= range_x:
                break
        if ground[yy+1][xr] not in ('.', '|'): # no exit at this end
            br = True
        else: # exit found
            if ground[yy][xr] == '.':
                area += 1
                ground[yy][xr] = '|'

        if not bl:
            area += flow(ground, yy, xl)

        if not br:
            area += flow(ground, yy, xr)

        if bl and br: # no exit found, convert to settled water:
            for xx in range(xl+1, xr):
                ground[yy][xx] = '~'
        else:
            break

    return area

area = flow(ground, 0, 500)
print(area)

for line in ground:
    print(''.join(line))
