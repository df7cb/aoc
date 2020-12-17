#!/usr/bin/python3

import re

width = 50
height = 6
#width = 8
#height = 3
board = [['.'] * width for x in range(height)]

def dump(board):
    for line in board:
        print('|' + ''.join(line) + '|')

def rect(board, w, h):
    for y in range(h):
        board[y][:w] = '#' * w

def rotate_row(board, y, d):
    board[y] = board[y][-d:] + board[y][:len(board[y])-d]

def rotate_column(board, x, d):
    column = [board[y][x] for y in range(len(board))]
    column = column[-d:] + column[:len(column)-d]
    for y in range(len(column)):
        board[y][x] = column[y]

dump(board)
with open('08.txt') as f:
    for line in f:
        print(line.strip())
        if m := re.match('rect (\d+)x(\d+)', line):
            rect(board, int(m[1]), int(m[2]))
        elif m := re.match('rotate row y=(\d+) by (\d+)', line):
            rotate_row(board, int(m[1]), int(m[2]))
        elif m := re.match('rotate column x=(\d+) by (\d+)', line):
            rotate_column(board, int(m[1]), int(m[2]))
        else:
            raise
        dump(board)

brightness = 0
for y in range(len(board)):
    for x in range(len(board[y])):
        if board[y][x] == '#':
            brightness += 1
print(brightness)
