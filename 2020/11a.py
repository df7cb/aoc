#!/usr/bin/python3

seats = []

with open('11.txt') as f:
    for line in f:
        seats.append(list(line))

print(seats)

def neighbors(seats, y, x):
    n = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            if x + dx < 0 or x + dx >= len(seats[y]):
                continue
            if y + dy < 0 or y + dy >= len(seats):
                continue
            if seats[y+dy][x+dx] == '#':
                n += 1
    return n

def update(seats):
    newseats = []
    updated = False
    for y in range(len(seats)):
        newseats.append([])
        for x in range(len(seats[y])):
            if seats[y][x] == 'L' and neighbors(seats, y, x) == 0:
                newseats[y].append('#')
                updated = True
            elif seats[y][x] == '#' and neighbors(seats, y, x) >= 4:
                newseats[y].append('L')
                updated = True
            else:
                newseats[y].append(seats[y][x])
    return updated, newseats

updated = True
rounds = 0
while updated:
    updated, seats = update(seats)
    rounds += 1
    print(seats)

count = 0
for y in range(len(seats)):
    for x in range(len(seats[y])):
        if seats[y][x] == '#':
            count += 1
print(rounds, count)
