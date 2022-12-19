#!/usr/bin/python3

import re

def dist(x, y, a, b):
    return abs(x - a) + abs(y - b)

sensors = []

with open("15.txt") as f:
    for line in f:
        m = re.match('Sensor at x=([-\d]+), y=([-\d]+): closest beacon is at x=([-\d]+), y=([-\d]+)', line)
        sensor = [int(x) for x in m.groups()]
        sensor.append(dist(*sensor))
        sensors.append(sensor)
sensors.sort(key = lambda x: -x[4])

#print(sensors)

#for xr in range(-10, 30):
#    print(xr % 10, end='')
#print()

num = 0
yr = 2000000
xr = -10000000
while True:
    if xr % 100000 == 0:
        print(xr, "found", num)
    found = False
    skipdist = 100000000
    for sensor in sensors:
        x, y, a, b, d = sensor
        if xr == a and yr == b:
            continue
        dr = abs(x - xr) + abs(y - yr)

        if dr <= d:
            if not found:
                num += 1
            found = True
        skipdist = min(skipdist, max(dr - d - 2, 1))

    if skipdist > 1:
        print("skipping", skipdist)
    xr += skipdist
    if xr > 20000000:
        break

    #print('#' if found else '.', end='')

print(f" {num}")

