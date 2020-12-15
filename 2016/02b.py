#!/usr/bin/python3

pad = [
[' ', ' ', '1', ' ', ' '],
[' ', '2', '3', '4', ' '],
['5', '6', '7', '8', '9'],
[' ', 'A', 'B', 'C', ' '],
[' ', ' ', 'D', ' ', ' ']]

def chew(line):
    x, y = 0, 2
    for char in line:
        if char == 'U' and y > 0 and pad[y-1][x] != ' ':
            y -= 1
        elif char == 'D' and y < 4 and pad[y+1][x] != ' ':
            y += 1
        elif char == 'L' and x > 0 and pad[y][x-1] != ' ':
            x -= 1
        elif char == 'R' and x < 4 and pad[y][x+1] != ' ':
            x += 1

    key = pad[y][x]
    print(key)

with open('02.txt') as f:
    for line in f:
        chew(line)
