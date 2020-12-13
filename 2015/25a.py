#!/usr/bin/python3

messages = "To continue, please consult the code grid in the manual.  Enter the code at row 2978, column 3083."

row, column = 2978, 3083

def number(row, column):
    diagonal = row + column - 1 # cell is in nth diagonal
    diagonal_top = int(diagonal * (diagonal+1) / 2) # number of cell (1, diagonal)
    return diagonal_top - (row - 1)

def code(row, column):
    seed = 20151125
    n = number(row, column)
    print(n)
    c = seed
    for x in range(1, n):
        c = step(c)
    return c

def step(code):
    return (code * 252533) % 33554393

print(code(row, column))
