#!/usr/bin/python3

puzzle = [int(x) for x in '496138527']
#puzzle = [int(x) for x in '389125467']

def move(puzzle, current):
    current_index = puzzle.index(current)
    l = len(puzzle)
    #print(puzzle, current, current_index)
    three_cups = (puzzle+puzzle)[current_index+1:current_index+4]
    print("pick up:", three_cups)
    for x in three_cups:
        puzzle.remove(x)

    destination = (current - 2) % l + 1
    while destination in three_cups:
        destination = (destination - 2) % l + 1
    print('destination:', destination)
    destination_index = puzzle.index(destination)
    puzzle[destination_index+1:destination_index+1] = three_cups

    current_index = puzzle.index(current)
    new_current = puzzle[(current_index + 1) % l]
    return new_current

current = puzzle[0]
for i in range(1, 101):
    print("-- move", i, "--")
    print("cups: ", end='')
    for x in puzzle:
        if x == current:
            print(f"({x})", end='')
        else:
            print(f" {x} ", end='')
    print()
    #print(puzzle, current)
    current = move(puzzle, current)
    print()

print('-- final --')
print('cups: ', end='')
for x in puzzle:
    if x == current:
        print(f"({x})", end='')
    else:
        print(f" {x} ", end='')
print()

one = puzzle.index(1)
out = puzzle[one+1:] + puzzle[:one]
print("".join([str(x) for x in out]))
