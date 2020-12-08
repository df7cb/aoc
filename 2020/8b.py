#!/usr/bin/python3

import re

mem = []

with open('8.txt') as f:
    for rule in f:
        m = re.match('(nop|acc|jmp) ([+-]\d+)', rule)
        mem.append({'cmd': m.group(1), 'val': int(m.group(2))})

#print(mem)

def run(tweak):
    acc = 0
    pc = 0
    visited = {}

    while True:
        if pc in visited:
            #print ('tweak', tweak, 'would execute instruction at', pc, 'again, acc is', acc)
            return
        visited[pc] = 1

        if pc == len(mem):
            print ('tweak', tweak, 'reached', pc, 'and acc is', acc)
            return
        elif pc > len(mem):
            print ('tweak', tweak, 'overflowed reached', pc, 'and acc is', acc)
            return

        cmd = mem[pc]['cmd']
        val = mem[pc]['val']
        #print(pc, acc, cmd, val)

        if cmd == 'nop' and tweak != pc or cmd == 'jmp' and tweak == pc:
            pc += 1
        elif cmd == 'acc':
            acc += val
            pc += 1
        elif cmd == 'jmp' and tweak != pc or cmd == 'nop' and tweak == pc:
            pc += val
        else:
            raise('invalid opcode', cmd)

for i in range(len(mem)):
    run(i)
