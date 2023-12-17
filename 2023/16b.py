#!/usr/bin/python3

with open("16.txt") as f:
    contraption = [line.strip() for line in f]

energized = set()
seen = set()

def run(energized, seen, y, x, dy, dx):
    while True:
        if (y, x, dy, dx) in seen:
            return energized
        seen.add((y, x, dy, dx))
        if y < 0 or y >= len(contraption) or x < 0 or x >= len(contraption[0]):
            return energized

        energized.add((y,x))
        if contraption[y][x] == '-' and dx == 0:
            run(energized, seen, y, x-1, 0, -1)
            run(energized, seen, y, x+1, 0, 1)
            return energized
        elif contraption[y][x] == '|' and dy == 0:
            run(energized, seen, y-1, x, -1, 0)
            run(energized, seen, y+1, x,  1, 0)
            return energized
        elif contraption[y][x] == '/':
            dy, dx = -dx, -dy
        elif contraption[y][x] == '\\':
            dy, dx = dx, dy

        y += dy
        x += dx

best = 0

for y in range(len(contraption)):
    energized = run(set(), set(), y, 0, 0, 1)
    best = max(best, len(energized))
    print(len(energized))
    energized = run(set(), set(), y, len(contraption[0])-1, 0, -1)
    best = max(best, len(energized))
    print(len(energized))
print()

for x in range(len(contraption[0])):
    energized = run(set(), set(), 0, x, 1, 0)
    best = max(best, len(energized))
    print(len(energized))
    energized = run(set(), set(), len(contraption)-1, x, -1, 0)
    best = max(best, len(energized))
    print(len(energized))
print()

print(best)
