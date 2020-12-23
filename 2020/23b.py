#!/usr/bin/python3

import array

#size = 9
size = 1000000
#rounds = 10
rounds = 10000000
puzzle_input = [int(x) for x in '496138527']
#puzzle_input = [int(x) for x in '389125467']
print(puzzle_input)

# index i represents cup i, value is next cup clockwise (credit: https://tinyurl.com/y9og6rrb)
puzzle = array.array('l', range(1, size+2))
puzzle[0] = 0 # not used
puzzle[-1] = puzzle_input[0]
#print(puzzle)

for i in range(len(puzzle_input)):
    this = puzzle_input[i]
    if i < len(puzzle_input)-1:
        next = puzzle_input[i+1]
    elif i < len(puzzle)-2: # last element of input before 1000000 array
        next = i+2
    else: # last element of input, and no extra 1000000 array
        next = puzzle_input[0]
    puzzle[this] = next

#print('index:    ', list(range(len(puzzle))))
#print(puzzle)

def move(puzzle, current):
    #print(puzzle, current)
    three_cups = []
    right = puzzle[current]; three_cups.append(right)
    right = puzzle[right]; three_cups.append(right)
    right = puzzle[right]; three_cups.append(right)
    right = puzzle[right]
    puzzle[current] = right
    #print("pick up:", three_cups)

    destination = current - 1
    if destination == 0:
        destination = size
    while destination in three_cups:
        destination -= 1
        if destination == 0:
            destination = size
    #print('destination:', destination)

    old_destination_next = puzzle[destination]
    puzzle[destination] = three_cups[0]
    puzzle[three_cups[2]] = old_destination_next

    return puzzle[current]

def print_cups(puzzle, current):
    print("cups: ", end='')
    this = current
    while True:
        if this == current:
            print(f"({this})", end='')
        else:
            print(f" {this} ", end='')
        this = puzzle[this]
        if this == current:
            break
    print()

current = puzzle_input[0]
for i in range(1, rounds+1):
    if i % 100000 == 0:
        print(i, current)
    #print("-- move", i, "--")
    #print_cups(puzzle, current)
    current = move(puzzle, current)
    #print()

print('-- final --')
#print_cups(puzzle, current)

first = puzzle[1]
second = puzzle[first]
print(first, second, first * second)
