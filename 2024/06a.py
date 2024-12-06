#!/usr/bin/python3

with open("06.txt") as f:
    lab = [line.strip() for line in f]

for y in range(len(lab)):
    if '^' in lab[y]:
        x = lab[y].index('^')
        dx = 0
        dy = -1
        visited = set([(y, x)])
        break

while True:
    if x + dx < 0 or \
       x + dx >= len(lab[0]) or \
       y + dy < 0 or \
       y + dy >= len(lab): break
    elif lab[y + dy][x + dx] == '#':
        dy, dx = dx, -dy
    else:
        y, x = y + dy, x + dx
        visited.add((y, x))

print(visited)
print(len(visited))
