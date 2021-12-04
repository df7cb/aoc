#!/usr/bin/python3

import re

with open('04.txt') as f:
    numbers = [int(x) for x in f.readline().split(',')]
    f.readline()
    boards = f.read(10000).split('\n\n')
    boards = [[[int(x) for x in line.split()] for line in board.splitlines()] for board in boards]

print(numbers)
print(boards)

def draw(board, number):
    for line in board:
        for pos in range(len(line)):
            if line[pos] == number:
                line[pos] = 0

def check(board):
    for line in board:
        if line == [0, 0, 0, 0, 0]:
            return True
    for y in range(5):
        if [board[x][y] for x in range(5)] == [0, 0, 0, 0, 0]:
            return True
    return False

def value(board):
    s = 0
    for line in board:
        s += sum(line)
    return s

for number in numbers:
    for board in boards:
        draw(board, number)
        if check(board):
            print("Winner:", board)
            print(number * value(board))
            exit(0)
