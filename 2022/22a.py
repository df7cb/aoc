#!/usr/bin/python3

import re

board = [list(' ' * 152)]

with open("22.txt") as f:
    for line in f:
        if line == '\n':
            break
        board += [list(' ' + line.rstrip() + ' ' * 102)]
    board += [list(' ' * 152)]

    steps = f.readline().strip()

y = 1
for x in range(len(board[0])):
    if board[y][x] != ' ':
        break
board[y][x] = 'x'
dx, dy = 1, 0

for line in board:
    print(''.join(line).rstrip())
print(steps)
print(y, x)

for n, d in re.findall('(\d+)([RL]?)', steps):
    print(n, d)
    for i in range(int(n)):
        nx, ny = x+dx, y+dy
        # wrap around
        if board[ny][nx] == ' ':
            if dx == 1:
                while board[ny][nx-1] != ' ':
                    nx -= 1
            elif dx == -1:
                while board[ny][nx+1] != ' ':
                    nx += 1
            elif dy == 1:
                while board[ny-1][nx] != ' ':
                    ny -= 1
            elif dy == -1:
                while board[ny+1][nx] != ' ':
                    ny += 1
        if board[ny][nx] in ('.', 'x'):
            y, x = ny, nx
            board[y][x] = 'x'
        else:
            print(f"blocked at step {i}")
            break

    if d == 'L': # 1 0 -> 0 -1, 0 1 -> 1 0, -1 0 -> 0 1
        dx, dy = dy, -dx
    elif d == 'R': # 1 0 -> 0 1, 0 1 -> -1 0, -1 0 -> 0 -1
        dx, dy = -dy, dx

    print(y, x, dy, dx)
    #for line in board:
    #    print(''.join(line).rstrip())

if (dx, dy) == (1, 0):
    dd = 0
elif (dx, dy) == (0, 1):
    dd = 1
elif (dx, dy) == (-1, 0):
    dd = 2
elif (dx, dy) == (0, -1):
    dd = 3

for line in board:
    print(''.join(line).rstrip())
print(1000 * y + 4 * x + dd)
