#!/usr/bin/python3

orbit = {}

with open("06.txt") as f:
    for line in f:
        a, b = line.strip().split(')')
        if a not in orbit:
            orbit[a] = []
        orbit[a].append(b)

print(orbit)

def orbits(planet):
    if planet not in orbit:
        return 0
    o = 0
    for orbiter in orbit[planet]:
        
