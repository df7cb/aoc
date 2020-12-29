#!/usr/bin/python3

import re

reg = {
        #"a": 7,
        "a": 12,
        "b": 0,
        "c": 0,
        "d": 0,
      }

pc = 0
mem = []

with open('23.txt') as f:
    for rule in f:
        if m := re.match('(cpy|jnz|add) (\S+) (\S+)', rule):
            mem.append(list(m.groups()))
        elif m := re.match('(inc|dec|tgl) (\S+)', rule):
            mem.append(list(m.groups()))
        else:
            raise SyntaxError(rule)

print(mem)

def val(expr):
    if expr in reg:
        return reg[expr]
    else:
        return int(expr)

c = 0
while True:
    cmd = mem[pc]
    if c % 3000001 == 0:
        print(c, pc, reg, cmd)

    if pc == 4:
        print(c, pc, reg, cmd)
        print('catching')
        reg['a'] = reg['b'] * reg['d']
        reg['c'] = 0
        reg['d'] = 0
        pc = 10
        print(c, pc, reg, cmd)
    elif cmd[0] == 'cpy':
        reg[cmd[2]] = val(cmd[1])
        pc += 1
    elif cmd[0] == 'add':
        reg[cmd[2]] += val(cmd[1])
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
            print(pc, 'tgl', dst, mem[dst], '->', end=' ')
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
            print(mem[dst])
        else:
            print(pc, 'skip tgl', dst)
        pc += 1
    else:
        raise SyntaxError('invalid opcode', cmd)

    if pc >= len(mem):
        break

    c += 1

print('23a:', c, pc, reg)
