#!/usr/bin/python3

with open("07.txt") as f:
    splitter = [list(line.strip()) for line in f.readlines()]

for line in splitter:
    print(line)

splits = 0

for i in range(1, len(splitter)):
    for j in range(len(splitter[0])):
        if splitter[i][j] == '.' and splitter[i-1][j] in ('|', 'S'):
            splitter[i][j] = '|'
        elif splitter[i][j] == '^' and splitter[i-1][j] == '|':
            splitter[i][j-1] = '|'
            splitter[i][j+1] = '|'
            splits += 1

for line in splitter:
    print(line)

print(splits)
