#!/usr/bin/python3

seats = []

with open('11.txt') as f:
    for line in f:
        seats.append(list(line.strip()))

print(seats)

def neighbors(seats, y, x):
    n = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            for dist in range(1, len(seats)):
                if x + dist*dx < 0 or x + dist*dx >= len(seats[y]):
                    break
                if y + dist*dy < 0 or y + dist*dy >= len(seats):
                    break
                if seats[y+dist*dy][x+dist*dx] == 'L':
                    break
                if seats[y+dist*dy][x+dist*dx] == '#':
                    n += 1
                    break
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
            elif seats[y][x] == '#' and neighbors(seats, y, x) >= 5:
                newseats[y].append('L')
                updated = True
            else:
                newseats[y].append(seats[y][x])
    return updated, newseats

updated = True
rounds = 0
while updated:
    rounds += 1
    print(rounds)
    updated, seats = update(seats)
    print(seats)

count = 0
for y in range(len(seats)):
    for x in range(len(seats[y])):
        if seats[y][x] == '#':
            count += 1
print(rounds, count)
