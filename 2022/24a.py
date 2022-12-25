#!/usr/bin/python3

with open("24.txt") as f:
    valley = [list(line.strip()[1:-1]) for line in f]
    valley = valley[1:-1]

winds = []
for line in range(len(valley)):
    for col in range(len(valley[line])):
        if valley[line][col] != '.':
            winds.append([line, col, valley[line][col]])

def print_valley(valley):
    for line in valley:
        print(''.join(line))
    print()

print_valley(valley)

posy, posx = (-1, 0)
queue = set([(posy, posx)])

t = 0
while True:
    t += 1
    valley2 = [['.' for x in line] for line in valley]

    for wind in winds:
        line, col, direction = wind
        if direction == '<':
            wind[1] = (col - 1) % len(valley[0])
        elif direction == '>':
            wind[1] = (col + 1) % len(valley[0])
        elif direction == '^':
            wind[0] = (line - 1) % len(valley)
        elif direction == 'v':
            wind[0] = (line + 1) % len(valley)
        valley2[wind[0]][wind[1]] = wind[2]

    queue2 = set()
    for posy, posx in queue:
        if posy < 0 or (posy >= 0 and valley2[posy][posx] == '.'):
            queue2.add((posy, posx))
            if posy >= 0:
                valley2[posy][posx] = 'E'
        if posy-1 >= 0 and valley2[posy-1][posx] == '.':
            queue2.add((posy-1, posx))
            valley2[posy-1][posx] = 'E'
        if posy+1 < len(valley) and valley2[posy+1][posx] == '.':
            queue2.add((posy+1, posx))
            valley2[posy+1][posx] = 'E'
        if posy >= 0 and posx-1 >= 0 and valley2[posy][posx-1] == '.':
            queue2.add((posy, posx-1))
            valley2[posy][posx-1] = 'E'
        if posy >= 0 and posx+1 < len(valley[0]) and valley2[posy][posx+1] == '.':
            queue2.add((posy, posx+1))
            valley2[posy][posx+1] = 'E'
        if posy == len(valley)-1 and posx == len(valley[0])-1:
            print(t)
            exit()

    valley = valley2
    queue = queue2
    print(t)
    print_valley(valley)
