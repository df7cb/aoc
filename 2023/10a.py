#!/usr/bin/python3

with open("10.txt") as f:
    field = [x.strip() for x in f]

for i in range(len(field)):
    if 'S' in field[i]:
        y = i
        x = field[i].index('S')

print(y, x)

# |-LJ7F

if field[y][x+1] in "-J7":
    (dy, dx) = (0, 1)
elif field[y+1][x] in "|LJ":
    (dy, dx) = (1, 0)
else:
    assert 0

print(dy, dx)
count = 0

while True:
    y += dy
    x += dx
    count += 1
    print(count, y, x, field[y][x])

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

print(int(count / 2))
