#!/usr/bin/python3

grid = []
moves = ''

with open("15.txt") as f:
    for line in f:
        if line.strip() == "": break
        l = []
        for c in line.strip():
            if c in ('#', '.'):
                l += [c, c]
            elif c == 'O':
                l += ['[', ']']
            elif c == '@':
                l += ['@', '.']
        grid.append(l)

    for line in f:
        moves += line.strip()

for line in grid: print(''.join(line))

for y in range(len(grid)):
    if '@' in grid[y]:
        x = grid[y].index('@')
        break

def can_move(y, x, dy, dx):
    if grid[y+dy][x+dx] == '.':
        return True
    elif grid[y+dy][x+dx] == '#':
        return False
    elif dy == 0 and grid[y+dy][x+dx] in ('[', ']'):
        return can_move(y, x+2*dx, dy, dx)
    elif grid[y+dy][x+dx] == '[':
        assert dx == 0
        return can_move(y+dy, x, dy, dx) and can_move(y+dy, x+1, dy, dx)
    elif grid[y+dy][x+dx] == ']':
        assert dx == 0
        return can_move(y+dy, x-1, dy, dx) and can_move(y+dy, x, dy, dx)
    else:
        assert False

def move(y, x, dy, dx):
    assert grid[y][x] != '#'
    if grid[y][x] == '.': return
    elif dy == 0 and grid[y][x] in ('[', ']'):
        move(y, x+2*dx, dy, dx)
    elif grid[y][x] == '[':
        move(y+dy, x, dy, dx)
        if grid[y+dy][x+1] != ']':
            move(y+dy, x+1, dy, dx)
    elif grid[y][x] == ']':
        move(y+dy, x-1, dy, dx)
        move(y+dy, x, dy, dx)
    elif grid[y][x] == '@':
        move(y+dy, x+dx, dy, dx)

    if dy != 0 and grid[y][x] == '[':
        grid[y+dy][x] = '['
        grid[y+dy][x+1] = ']'
        grid[y][x] = '.'
        grid[y][x+1] = '.'
    if dy != 0 and grid[y][x] == ']':
        grid[y+dy][x-1] = '['
        grid[y+dy][x] = ']'
        grid[y][x-1] = '.'
        grid[y][x] = '.'
    elif dy == 0 and grid[y][x] == '[':
        assert dx == 1
        grid[y][x+1] = '['
        grid[y][x+2] = ']'
        grid[y][x] = '.'
    elif dy == 0 and grid[y][x] == ']':
        assert dx == -1
        grid[y][x-2] = '['
        grid[y][x-1] = ']'
        grid[y][x] = '.'
    elif grid[y][x] == '@':
        grid[y+dy][x+dx] = grid[y][x]
        grid[y][x] = '.'

for mv in moves:
    if mv == '<': dy, dx = 0, -1
    elif mv == '>': dy, dx = 0, 1
    elif mv == '^': dy, dx = -1, 0
    elif mv == 'v': dy, dx = 1, 0

    print(y, x, mv)
    #for line in grid: print(''.join(line))

    if can_move(y, x, dy, dx):
        print('can move')
        move(y, x, dy, dx)
        x += dx
        y += dy

for line in grid: print(''.join(line))

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '[':
            total += 100 * y + x
print(total)
