#!/usr/bin/python3

import re

program = []

with open('24.txt') as f:
    for line in f:
        fields = line.split()
        if line == "\n":
            pass
        elif fields[0] == 'inp':
            program.append([])
        else:
            program[-1].append(fields)

print(program)

reg = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }

monad = [1 for x in range(14)]

def inp():
    return monad.pop()

def rg(x, reg):
    if m := re.match('[wxyz]', x):
        return reg[x]
    else:
        return int(x)

def run(op, reg):
    if op[0] == 'inp':
        reg[op[1]] = inp()
    elif op[0] == 'add':
        reg[op[1]] = reg[op[1]] + rg(op[2], reg)
    elif op[0] == 'mul':
        reg[op[1]] = reg[op[1]] * rg(op[2], reg)
    elif op[0] == 'div':
        reg[op[1]] = reg[op[1]] // rg(op[2], reg)
    elif op[0] == 'mod':
        reg[op[1]] = reg[op[1]] % rg(op[2], reg)
    elif op[0] == 'eql':
        reg[op[1]] = int(reg[op[1]] == rg(op[2], reg))
    else:
        print("op", op)
        assert(0)

def prg_sub(program, reg):
    for op in program:
        #print(op)
        run(op, reg)
        #print("         ", reg)
    return reg

def run_dummy(reg, w, c, a, b):
    z = reg['z']
    reg['w'] = w
    reg['x'] = int(reg['z']%26+a != w)
    reg['y'] = (w+b) * (((z%26)+a) != w)
    reg['z'] = (reg['z']//c) * (25 * (reg['z'] % 26 + a != w) + 1) * (w + b) * (reg['z'] % 26 + a != w)
    return reg

print("Real run: ", prg_sub(program[-1], { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }))
print("Dummy run:", run_dummy({ 'w': 0, 'x': 0, 'y': 0, 'z': 0 }, 0, 1, 10, 15))
