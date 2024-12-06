#!/usr/bin/python3

with open("06.txt") as f:
    lab = [line.strip() for line in f]

for y in range(len(lab)):
    if '^' in lab[y]:
        x = lab[y].index('^')
        visited = set([(y, x)])
        break

def check(ey, ex, y, x):
    l = [list(line) for line in lab]
    l[ey][ex] = '#'

    dx = 0
    dy = -1
    visited = set([(y, x, dy, dx)])

    while True:
        if x + dx < 0 or \
           x + dx >= len(l[0]) or \
           y + dy < 0 or \
           y + dy >= len(l): break
        elif l[y + dy][x + dx] == '#':
            dy, dx = dx, -dy
        else:
            y, x = y + dy, x + dx
            if (y, x, dy, dx) in visited: return True
            visited.add((y, x, dy, dx))

    return False

positions = 0

for ey in range(len(lab)):
    for ex in range(len(lab[0])):
        if lab[ey][ex] == '.':
            if check(ey, ex, y, x):
                print(ey, ex)
                positions += 1

print(positions)
