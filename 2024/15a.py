#!/usr/bin/python3

grid = []
moves = ''

with open("15.txt") as f:
    for line in f:
        if line.strip() == "": break
        grid.append(list(line.strip()))

    for line in f:
        moves += line.strip()

for y in range(len(grid)):
    if '@' in grid[y]:
        x = grid[y].index('@')
        break

for move in moves:
    if move == '<': dy, dx = 0, -1
    elif move == '>': dy, dx = 0, 1
    elif move == '^': dy, dx = -1, 0
    elif move == 'v': dy, dx = 1, 0

    #print(y, x, move)
    #for line in grid: print(''.join(line))

    # count stones
    ds = 0
    while grid[y+(ds+1)*dy][x+(ds+1)*dx] == 'O':
        ds += 1
    # check if there's a wall
    if grid[y+(ds+1)*dy][x+(ds+1)*dx] == '#':
        continue
    # move stones
    grid[y+(ds+1)*dy][x+(ds+1)*dx] = 'O'
    # move robot
    grid[y][x] = '.'
    y += dy
    x += dx
    grid[y][x] = '@'

for line in grid: print(''.join(line))

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'O':
            total += 100 * y + x
print(total)
