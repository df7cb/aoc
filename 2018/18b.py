#!/usr/bin/python3

with open('18.txt') as f:
    wood = [list(line.strip()) for line in f]

def dump(wood):
    for line in wood:
        print("".join(line))

def serialize(wood):
    return "".join(["".join(line) for line in wood])

dump(wood)

def surrondings(wood, y, x):
    s = []

    if y > 0:
        if x > 0:
            s.append(wood[y-1][x-1])
        s.append(wood[y-1][x])
        if x < len(wood[0])-1:
            s.append(wood[y-1][x+1])

    if x > 0:
        s.append(wood[y][x-1])
    if x < len(wood[0])-1:
        s.append(wood[y][x+1])

    if y < len(wood)-1:
        if x > 0:
            s.append(wood[y+1][x-1])
        s.append(wood[y+1][x])
        if x < len(wood[0])-1:
            s.append(wood[y+1][x+1])

    return s

def step(wood):
    wood2 = [[wood[y][x] for x in range(len(wood[0]))] for y in range(len(wood))]

    for y in range(len(wood)):
        for x in range(len(wood[0])):
            if wood[y][x] == '.':
                if surrondings(wood, y, x).count('|') >= 3:
                    wood2[y][x] = '|'
            elif wood[y][x] == '|':
                if surrondings(wood, y, x).count('#') >= 3:
                    wood2[y][x] = '#'
            elif wood[y][x] == '#':
                if surrondings(wood, y, x).count('#') >= 1 and surrondings(wood, y, x).count('|') >= 1:
                    pass
                else:
                    wood2[y][x] = '.'

    return wood2

seen = { serialize(wood): 0 }

for minute in range(1, 10001):
    print(minute)
    wood = step(wood)
    ser = serialize(wood)
    dump(wood)
    if ser in seen:
        print("cycle found in minute", minute, ", was seen in", seen[ser])
        cycle = minute - seen[ser]
        print("cycle length is", cycle)
        break
    seen[ser] = minute

# continue
for minute2 in range(minute+1, 10001):
    print(minute2)
    wood = step(wood)
    if (1000000000 - minute2) % cycle == 0:
        break

wooded_acres, lumberyards = 0, 0
for line in wood:
    wooded_acres += line.count('|')
    lumberyards += line.count('#')

print(wooded_acres, lumberyards, wooded_acres * lumberyards)
