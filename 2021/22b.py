#!/usr/bin/python3

import re

init = []

with open('22.txt') as f:
    # on x=-16..31,y=1..46,z=-4..43
    for line in f:
        m = re.match('(on|off) x=([\d-]+)..([\d-]+),y=([\d-]+)..([\d-]+),z=([\d-]+)..([\d-]+)', line)
        c = [int(x) for x in m.groups()[1:]]
        init.append((m.group(1)=='on', (c[0], c[1]+1), (c[2], c[3]+1), (c[4], c[5]+1)))

cubes=set()

# xi[0]....................xi[1]
#                  xc[0]....................xc[1]

def overlaps(xi, yi, zi, xc, yc, zc):
    if xi[1] <= xc[0] or xc[1] <= xi[0] or \
       yi[1] <= yc[0] or yc[1] <= yi[0] or \
       zi[1] <= zc[0] or zc[1] <= zi[0]:
           return False
    return True

def weight(cubes):
    s = 0
    for x, y, z in cubes:
        assert(x[0] < x[1])
        assert(y[0] < y[1])
        assert(z[0] < z[1])
        s += (x[1]-x[0]) * (y[1]-y[0]) * (z[1]-z[0])
    return s

for op, xi, yi, zi in init:
    print(op, xi, yi, zi)
    overlap = True
    while overlap:
        overlap = False
        for xc, yc, zc in cubes:
            if overlaps(xi, yi, zi, xc, yc, zc):
                cubes.remove((xc, yc, zc))
                if xc[0] < xi[0] < xc[1]:
                    cubes.add(((xc[0], xi[0]), yc, zc))
                    cubes.add(((xi[0], xc[1]), yc, zc))
                elif xc[0] < xi[1] < xc[1]:
                    cubes.add(((xc[0], xi[1]), yc, zc))
                    cubes.add(((xi[1], xc[1]), yc, zc))
                elif yc[0] < yi[0] < yc[1]:
                    cubes.add((xc, (yc[0], yi[0]), zc))
                    cubes.add((xc, (yi[0], yc[1]), zc))
                elif yc[0] < yi[1] < yc[1]:
                    cubes.add((xc, (yc[0], yi[1]), zc))
                    cubes.add((xc, (yi[1], yc[1]), zc))
                elif zc[0] < zi[0] < zc[1]:
                    cubes.add((xc, yc, (zc[0], zi[0])))
                    cubes.add((xc, yc, (zi[0], zc[1])))
                elif zc[0] < zi[1] < zc[1]:
                    cubes.add((xc, yc, (zc[0], zi[1])))
                    cubes.add((xc, yc, (zi[1], zc[1])))
                #else: # init cube overlaps existing cube completely
                overlap = True
                #print(len(cubes), cubes)
                break
    if op:
        cubes.add((xi, yi, zi))
    print(len(cubes), weight(cubes))

print("Sum", weight(cubes))
