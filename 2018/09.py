#!/usr/bin/python3

import re
from math import sqrt

stars = []

#position=<-31761,  10798> velocity=< 3, -1>

with open('09.txt') as f:
    for line in f:
        if m := re.match('position=<([ \d-]+),([ \d-]+)> velocity=<([ \d-]+),([ \d-]+)>', line):
            stars.append([int(x) for x in m.groups()])

tick = 0

last_magniude = None

while True:
    tick += 1
    center = (0, 0)
    for star in stars:
        star[0] += star[2]
        star[1] += star[3]
        center = (center[0] + star[0], center[1] + star[1])

    center = (center[0] / len(stars), center[1] / len(stars))
    magnitude = 0
    for star in stars:
        magnitude += sqrt((star[0]-center[0])**2 + (star[1]-center[1])**2)

    print(tick, center, magnitude)
    if last_magniude and magnitude > last_magniude:
        break
    last_magniude = magnitude

# undo last step
max_x, max_y = 0, 0
for star in stars:
    star[0] -= star[2]
    star[1] -= star[3]
    max_x = max(max_x, star[0])
    max_y = max(max_y, star[1])

print(tick - 1, stars)

sky = [[' ' for x in range(max_x+1)] for y in range(max_y+1)]

for star in stars:
    sky[star[1]][star[0]] = '#'

for y in sky:
    print("".join(y))
