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

def run_dummy(reg, c, a, b):
    z = reg['z']
    w = reg['w']
    reg['x'] = int(reg['z']%26+a != w)
    reg['y'] = (w+b) * (((z%26)+a) != w)
    reg['z'] = (z//c) * (25 * (z%26+a!=w) + 1) + (w+b) * (z%26+a!=w)
    return reg

def chew(monad):
    reg = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }
    for x in range(len(monad)):
        reg['w'] = monad[x]
        reg = prg_sub(program[x], reg)
    #if reg['z'] > 10000: return
    print(x, monad[x], reg)

#for i in range(10000):
#    ii = [int(x) for x in f"{i:04}"]
#    if 0 in ii: continue
#    print("Trying", ii)
#    chew(ii)

chew([int(x) for x in '13579246899999'])

#for w in range(10):
#    print("Real run: ", prg_sub(program[0], { 'w': w, 'x': 0, 'y': 0, 'z': 0 }))
#    print("Dummy run:", run_dummy({ 'w': w, 'x': 0, 'y': 0, 'z': 0 }, 1, 10, 15))

#print()
#
#for w in range(10):
#    print("Real run: ", prg_sub(program[-1], { 'w': w, 'x': 0, 'y': 0, 'z': 0 }))
#    print("Dummy run:", run_dummy({ 'w': w, 'x': 0, 'y': 0, 'z': 0 }, 26, -11, 2))
