#!/usr/bin/python3

import re

reg = {
        "a": 0,
        "b": 0,
        "c": 1,
        "d": 0,
      }

pc = 0
mem = []

with open('12.txt') as f:
    for rule in f:
        if m := re.match('(cpy|jnz) (.+) (.+)', rule):
            mem.append(m.groups())
        elif m := re.match('(inc|dec) (.+)', rule):
            mem.append(m.groups())
        else:
            raise SyntaxError(rule)

print(mem)

def val(expr):
    if expr in reg:
        return reg[expr]
    else:
        return int(expr)

while True:
    cmd = mem[pc]
    #print(pc, reg, cmd)

    if cmd[0] == 'cpy':
        reg[cmd[2]] = val(cmd[1])
        pc += 1
    elif cmd[0] == 'inc':
        reg[cmd[1]] += 1
        pc += 1
    elif cmd[0] == 'dec':
        reg[cmd[1]] -= 1
        pc += 1
    elif cmd[0] == 'jnz':
        if val(cmd[1]) != 0:
            pc += val(cmd[2])
        else:
            pc += 1
    else:
        raise SyntaxError('invalid opcode', cmd)

    if pc >= len(mem):
        break

print('11b:', pc, reg)
