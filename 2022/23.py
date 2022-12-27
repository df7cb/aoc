#!/usr/bin/python3

elves = []

y = 0
with open("23.txt") as f:
    for line in f:
        x = 0
        for c in line.strip():
            if c == '#':
                elves.append([y, x, 0, 0])
            x += 1
        y += 1

print(elves)

directions = ['N', 'S', 'W', 'E']

def step(elves, directions):
    positions = {(elf[0], elf[1]) for elf in elves}

    for elf in elves:
        y, x, ny, nx = elf

        want_move = False
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy == dx == 0:
                    continue
                if (y+dy, x+dx) in positions:
                    want_move = True

        elf[2:] = [y, x]
        if want_move:
            for direction in directions:
                if direction == 'N' and (y-1,x-1) not in positions and (y-1,x) not in positions and (y-1, x+1) not in positions:
                    elf[2:] = [y-1,x]
                    break
                elif direction == 'S' and (y+1,x-1) not in positions and (y+1,x) not in positions and (y+1, x+1) not in positions:
                    elf[2:] = [y+1,x]
                    break
                elif direction == 'W' and (y-1,x-1) not in positions and (y,x-1) not in positions and (y+1, x-1) not in positions:
                    elf[2:] = [y,x-1]
                    break
                elif direction == 'E' and (y-1,x+1) not in positions and (y,x+1) not in positions and (y+1, x+1) not in positions:
                    elf[2:] = [y,x+1]
                    break

    any_elf_moved = False
    new_positions = [(elf[2], elf[3]) for elf in elves]
    for elf in elves:
        if elf[0:2] == elf[2:4]: continue
        if len([x for x in new_positions if x == (elf[2], elf[3])]) == 1:
            elf[0], elf[1] = elf[2], elf[3]
            any_elf_moved = True

    directions[:] = directions[1:] + [directions[0]]

    return any_elf_moved

def print_elves(elves):
    min_y = min([elf[0] for elf in elves])
    max_y = max([elf[0] for elf in elves])
    min_x = min([elf[1] for elf in elves])
    max_x = max([elf[1] for elf in elves])
    positions = {(elf[0], elf[1]) for elf in elves}

    #for y in range(min_y-1, max_y+3):
    for y in range(-2, max_y+3):
        #for x in range(min_x-1, max_x+3):
        for x in range(-3, max_x+3):
            if (y, x) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print((max_y-min_y+1) * (max_x-min_y+1) - len(elves))
    print()

n = 0
print('== Initial State ==')
print_elves(elves)
while True:
    n += 1
    any_elf_moved = step(elves, directions)
    print(f"== End of Round {n} ==")
    #print(elves, any_elf_moved, directions)
    print_elves(elves)
    if not any_elf_moved:
        break
