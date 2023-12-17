#!/usr/bin/python3

with open("16.txt") as f:
    contraption = [line.strip() for line in f]

energized = set()
seen = set()

def run(y, x, dy, dx):
    while True:
        if (y, x, dy, dx) in seen:
            return
        seen.add((y, x, dy, dx))
        if y < 0 or y >= len(contraption) or x < 0 or x >= len(contraption[0]):
            return

        energized.add((y,x))
        if contraption[y][x] == '-' and dx == 0:
            run(y, x-1, 0, -1)
            run(y, x+1, 0, 1)
            return
        elif contraption[y][x] == '|' and dy == 0:
            run(y-1, x, -1, 0)
            run(y+1, x,  1, 0)
            return
        elif contraption[y][x] == '/':
            dy, dx = -dx, -dy
        elif contraption[y][x] == '\\':
            dy, dx = dx, dy

        y += dy
        x += dx

run(0, 0, 0, 1)

for y in range(len(contraption)):
    for x in range(len(contraption[0])):
        if (y, x) in energized:
            print('#', end='')
        else:
            print(contraption[y][x], end='')
    print()

#print(seen)
#print(len(seen))
#print(sorted(energized))
print(len(energized))
