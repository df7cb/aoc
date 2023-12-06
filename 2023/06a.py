#!/usr/bin/python3

import re

with open("06.txt") as f:
    m = re.match('Time: (.*)', f.readline())
    times = [int(x) for x in m.group(1).split()]
    m = re.match('Distance: (.*)', f.readline())
    dists = [int(x) for x in m.group(1).split()]

print(times)
print(dists)

def check_race(time, dist):
    i = 0
    for t in range(time):
        speed = t
        traveltime = time - t
        distance = speed * traveltime
        if distance > dist:
            i += 1
    return i

factor = 1
for i in range(len(times)):
    wins = check_race(times[i], dists[i])
    print(times[i], dists[i], wins)
    factor *= wins

print(factor)
