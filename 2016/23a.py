#!/usr/bin/python3

import re

reg = {
        "a": 7,
        "b": 0,
        "c": 0,
        "d": 0,
      }

pc = 0
mem = []

with open('23.txt') as f:
    for rule in f:
        if m := re.match('(cpy|jnz) (.+) (.+)', rule):
            mem.append(list(m.groups()))
        elif m := re.match('(inc|dec|tgl) (.+)', rule):
            mem.append(list(m.groups()))
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
    print(pc, reg, cmd)

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
    elif cmd[0] == 'tgl':
        dst = pc + val(cmd[1])
        if 0 <= dst < len(mem):
            print('tgl', dst, mem[dst])
            if len(mem[dst]) == 2:
                if mem[dst][0] == 'inc':
                    mem[dst][0] = 'dec'
                else:
                    mem[dst][0] = 'inc'
            else:
                if mem[dst][0] == 'jnz':
                    mem[dst][0] = 'cpy'
                else:
                    mem[dst][0] = 'jnz'
        pc += 1
    else:
        raise SyntaxError('invalid opcode', cmd)

    if pc >= len(mem):
        break

print('23a:', pc, reg)
