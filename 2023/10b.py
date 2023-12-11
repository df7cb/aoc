#!/usr/bin/python3

with open("10.txt") as f:
    field0 = [[c for c in line.strip()] for line in f]

field = []
for line in field0:
    line2 = []
    for c in line:
        line2.append(' ')
        line2.append(c)
    line2.append(' ')
    field.append([' ' for x in line2])
    field.append(line2)
field.append([' ' for x in line2])

for i in range(len(field)):
    if 'S' in field[i]:
        y = i
        x = field[i].index('S')

def print_field(field):
    for line in field:
        print(''.join(line))

print_field(field)
print(y, x)

# |-LJ7F

if field[y][x+2] in "-J7":
    (dy, dx) = (0, 1)
elif field[y+2][x] in "|LJ":
    (dy, dx) = (1, 0)
else:
    assert 0

print(dy, dx)

while True:
    y += dy
    x += dx
    field[y][x] = 'x'
    y += dy
    x += dx
    print(y, x, field[y][x])

    if field[y][x] == 'S':
        break

    if (dy, dx) == (0, 1):
        if field[y][x] == 'J':
            (dy, dx) = (-1, 0)
        elif field[y][x] == '7':
            (dy, dx) = (1, 0)
        elif field[y][x] == '-':
            pass
        else:
            assert 0
    elif (dy, dx) == (0, -1):
        if field[y][x] == 'L':
            (dy, dx) = (-1, 0)
        elif field[y][x] == 'F':
            (dy, dx) = (1, 0)
        elif field[y][x] == '-':
            pass
        else:
            assert 0
    elif (dy, dx) == (-1, 0):
        if field[y][x] == 'F':
            (dy, dx) = (0, 1)
        elif field[y][x] == '7':
            (dy, dx) = (0, -1)
        elif field[y][x] == '|':
            pass
        else:
            assert 0
    elif (dy, dx) == (1, 0):
        if field[y][x] == 'L':
            (dy, dx) = (0, 1)
        elif field[y][x] == 'J':
            (dy, dx) = (0, -1)
        elif field[y][x] == '|':
            pass
        else:
            assert 0

    field[y][x] = 'x'

print_field(field)

queue = [(0, 0)]
seen = set(queue)
while queue:
    y, x = queue.pop()
    field[y][x] = 'x'
    seen.add((y, x))
    for y2, x2 in ((y, x+1), (y, x-1), (y-1, x), (y+1, x)):
        if x2 >= 0 and x2 < len(field[0]) and y2 >= 0 and y2 < len(field) and field[y2][x2] not in ('S', 'x') and (y2, x2) not in seen:
            queue.append((y2, x2))

print_field(field)

count = 0

for y in range(1, len(field), 2):
    for x in range(1, len(field[0]), 2):
        if field[y][x] not in ('S', 'x'):
            count += 1

print(count)
