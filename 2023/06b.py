#!/usr/bin/python3

import re

with open("06.txt") as f:
    m = re.match('Time: (.*)', f.readline())
    time = int(m.group(1).replace(' ', ''))
    m = re.match('Distance: (.*)', f.readline())
    dist = int(m.group(1).replace(' ', ''))

print(time)
print(dist)

def check_race(time, dist):
    i = 0
    for t in range(time):
        speed = t
        traveltime = time - t
        distance = speed * traveltime
        if distance > dist:
            i += 1
    return i

print(check_race(time, dist))
