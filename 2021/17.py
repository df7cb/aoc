#!/usr/bin/python3

import re

inp = 'target area: x=240..292, y=-90..-57'
#inp = 'target area: x=20..30, y=-10..-5'

m = re.match('target area: x=([\d-]+)..([\d-]+), y=([\d-]+)..([\d-]+)', inp)
x1, x2, y1, y2 = [int(x) for x in m.groups()]

def run(dx, dy):
    x, y = 0, 0
    max_y = 0
    while True:
        x += dx
        y += dy
        if dx > 0:
            dx -= 1
        dy -= 1

        max_y = max(max_y, y)

        #print(x, y)
        if y < y1 or x > x2:
            return False, max_y

        if x1 <= x <= x2 and y1 <= y <= y2:
            return True, max_y

working = 0
max_max_y = 0
for dy in range(y1, abs(y1)+1): # min y so we don't overshoot on the first step, max y since on descent, we will hit y=0 and y=-dy
    #print(dy)
    for dx in range(x2+1): # can't shoot harder than that or we overshoot in the first step
        hit, max_y = run(dx, dy)
        if hit and max_y > max_max_y:
            max_max_y = max_y
        if hit:
            working += 1
            print(working, dx, dy, hit, max_y, max_max_y)
    dy += 1

