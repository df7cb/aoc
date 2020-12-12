#!/usr/bin/python3

import re

mem = []
pc = 0
reg = {
        "a": 0, # 23a
        #"a": 1, # 23b
        "b": 0,
}

with open('23.txt') as f:
    mem = f.readlines()

while 0 <= pc < len(mem):
    print(pc, reg['a'], reg['b'], mem[pc].strip())
    if m := re.match('hlf ([ab])', mem[pc]):
        reg[m[1]] = int(reg[m[1]]/2)
        pc += 1
    elif m := re.match('tpl ([ab])', mem[pc]):
        reg[m[1]] *= 3
        pc += 1
    elif m := re.match('inc ([ab])', mem[pc]):
        reg[m[1]] += 1
        pc += 1
    elif m := re.match('jmp ([+-]\d+)', mem[pc]):
        pc += int(m[1])
    elif m := re.match('jie ([ab]), ([+-]\d+)', mem[pc]):
        if reg[m[1]] % 2 == 0:
            pc += int(m[2])
        else:
            pc += 1
    elif m := re.match('jio ([ab]), ([+-]\d+)', mem[pc]):
        if reg[m[1]] == 1:
            pc += int(m[2])
        else:
            pc += 1
    else:
        raise

print(pc, reg['a'], reg['b'])
