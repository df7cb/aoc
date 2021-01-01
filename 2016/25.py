#!/usr/bin/python3

import re

reg = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
      }

mem = []

with open('25.txt') as f:
    for rule in f:
        if m := re.match('(cpy|jnz) (.+) (.+)', rule):
            mem.append(m.groups())
        elif m := re.match('(inc|dec|out) (.+)', rule):
            mem.append(m.groups())
        else:
            raise SyntaxError(rule)

print(mem)

def run(reg):
    pc = 0

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
        elif cmd[0] == 'out':
            yield reg[cmd[1]]
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

def run_with_a(a):
    expect = None
    c = 0
    for v in run({ "a": a, "b": 0, "c": 0, "d": 0 }):
        if expect is None:
            expect = v
        if c % 1000 == 999:
            print(c, expect, v, reg)
        if c == 1000:
            print("25: Looks like it's", a)
            exit(0)
        if v != expect:
            print(reg, v, 'mismatch', expect, 'in cycle', c)
            break
        expect = 0 if v else 1
        c += 1

a = 0
while True:
    print('Trying', a)
    run_with_a(a)
    a += 1
