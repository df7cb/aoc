#!/usr/bin/python3

with open("10.txt") as f:
    m = [[int(x) for x in line.strip()] for line in f]

def trailhead(y, x, nines):
    if m[y][x] == 9:
        nines.add((y, x))
        return
    if y > 0 and m[y-1][x] == m[y][x] + 1:
        trailhead(y-1, x, nines)
    if y < len(m)-1 and m[y+1][x] == m[y][x] + 1:
        trailhead(y+1, x, nines)
    if x > 0 and m[y][x-1] == m[y][x] + 1:
        trailhead(y, x-1, nines)
    if x < len(m[0])-1 and m[y][x+1] == m[y][x] + 1:
        trailhead(y, x+1, nines)

score = 0

for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == 0:
            nines = set()
            trailhead(y, x, nines)
            print(y, x, len(nines))
            score += len(nines)

print(score)
