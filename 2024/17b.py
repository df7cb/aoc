#!/usr/bin/python3

import re

reg = {}

with open("17.txt") as f:
    m = re.match(r'Register (.): (\d+)', f.readline())
    reg[m.group(1)] = int(m.group(2))
    m = re.match(r'Register (.): (\d+)', f.readline())
    reg[m.group(1)] = int(m.group(2))
    m = re.match(r'Register (.): (\d+)', f.readline())
    reg[m.group(1)] = int(m.group(2))
    f.readline()
    m = re.match(r'Program: (.+)', f.readline())
    prog = [int(x) for x in m.group(1).split(',')]

print(reg)
print(prog)

def combo(val, reg):
    assert val < 7
    if val <= 3: return val
    elif val == 4: return reg['A']
    elif val == 5: return reg['B']
    elif val == 6: return reg['C']

def run(reg):
    ip = 0
    output = []

    while ip < len(prog)-1:
        opcode = prog[ip]
        operand = prog[ip+1]
        #print(ip, opcode, operand, reg)
        if opcode == 0: # adv
            reg['A'] = reg['A'] >> combo(operand, reg)
        elif opcode == 1: # bxl
            reg['B'] = reg['B'] ^ operand
        elif opcode == 2: # bst
            reg['B'] = combo(operand, reg) % 8
        elif opcode == 3: # jnz
            if reg['A'] != 0:
                ip = operand
                continue # skip ip+2
        elif opcode == 4: # bxc
            reg['B'] = reg['B'] ^ reg['C']
        elif opcode == 5: # out
            out = combo(operand, reg) % 8
            output.append(out)
        elif opcode == 6: # bdv
            reg['B'] = reg['A'] >> combo(operand, reg)
        elif opcode == 7: # cdv
            reg['C'] = reg['A'] >> combo(operand, reg)
        ip += 2
        #input()

    return output

a = 0
while True:
    out = run({'A': a, 'B': reg['B'], 'C': reg['C']})
    if a % 1000 == 0: print(a, out)
    if out == prog: break
    a += 1
