#!/usr/bin/python3

ant = {}

with open("08.txt") as f:
    y = 0
    for line in f:
        x = 0
        for c in line.strip():
            if c != '.':
                if c not in ant:
                    ant[c] = []
                ant[c].append((y, x))
            x += 1
        y += 1

print(y, x, ant)

antinodes = set()

for freq in ant:
    for a in ant[freq]:
        for b in ant[freq]:
            if a == b: continue
            print(a, b)
            c = (2 * b[0] - a[0], 2 * b[1] - a[1])
            if c[0] < 0 or c[0] >= y or c[1] < 0 or c[1] >= x: continue
            antinodes.add(c)

print(antinodes)
print(len(antinodes))
