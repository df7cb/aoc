#!/usr/bin/python3

import re

acc = 0
pc = 0
mem = []

with open('08.txt') as f:
    for rule in f:
        m = re.match('(nop|acc|jmp) ([+-]\d+)', rule)
        mem.append({'cmd': m.group(1), 'val': int(m.group(2))})

print(mem)

while True:
    cmd = mem[pc]['cmd']
    val = mem[pc]['val']
    print(pc, acc, cmd, val)

    if 'visited' in mem[pc]:
        print ('would execute instruction at', pc, 'again, acc is', acc)
        exit(0)
    mem[pc]['visited'] = 1

    if cmd == 'nop':
        pc += 1
    elif cmd == 'acc':
        acc += val
        pc += 1
    elif cmd == 'jmp':
        pc += val
    else:
        raise('invalid opcode', cmd)

