#!/usr/bin/python3

import re

def op(reg, code, a, b, c):
    if code == 0: # addr (add register) stores into register C the result of adding register A and register B.
        res = reg[a] + reg[b]
    elif code == 1: # addi (add immediate) stores into register C the result of adding register A and value B.
        res = reg[a] + b
    elif code == 2: # mulr (multiply register) stores into register C the result of multiplying register A and register B.
        res = reg[a] * reg[b]
    elif code == 3: # muli (multiply immediate) stores into register C the result of multiplying register A and value B.
        res = reg[a] * b
    elif code == 4: # banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
        res = reg[a] & reg[b]
    elif code == 5: # bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
        res = reg[a] & b
    elif code == 6: # borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
        res = reg[a] | reg[b]
    elif code == 7: # bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
        res = reg[a] | b
    elif code == 8: # setr (set register) copies the contents of register A into register C. (Input B is ignored.)
        res = reg[a]
    elif code == 9: # seti (set immediate) stores value A into register C. (Input B is ignored.)
        res = a
    elif code == 10: # gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
        res = a > reg[b]
    elif code == 11: # gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
        res = reg[a] > b
    elif code == 12: # gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
        res = reg[a] > reg[b]
    elif code == 13: # eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
        res = a == reg[b]
    elif code == 14: # eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
        res = reg[a] == b
    elif code == 15: # eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
        res = reg[a] == reg[b]

    reg2 = [x for x in reg]
    reg2[c] = int(res)
    return reg2

opcodes = {}

def check(before, after, code, a, b, c):
    valid_codes = set()
    for cd in range(16):
        run = op(before, cd, a, b, c)
        if run == after:
            valid_codes.add(cd)

    new_opcodes = valid_codes - {x for x in opcodes.values()}
    if len(new_opcodes) == 1:
        print("Learned", code, "is", new_opcodes, valid_codes, before, after, code, a, b, c)
        opcodes[code] = min(new_opcodes)

testcases = []
cmd = []

with open('16.txt') as f:
    for line in f:
        if m := re.match('Before: \[(\d+), (\d+), (\d+), (\d+)\]', line):
            before = [int(x) for x in m.groups()]
        elif m := re.match('(\d+) (\d+) (\d+) (\d+)', line):
            cmd.append([int(x) for x in m.groups()])
        elif m := re.match('After:  \[(\d+), (\d+), (\d+), (\d+)\]', line):
            after = [int(x) for x in m.groups()]
            testcases.append([before, cmd[0], after])
            cmd = []

for testcase in testcases:
    check(testcase[0], testcase[2], *testcase[1])

print("I know about", len(opcodes), "opcodes now:", opcodes)

reg = [0, 0, 0, 0]

for c in cmd:
    c2 = [opcodes[c[0]], *c[1:]]
    reg = op(reg, *c2)
    print(reg, c2)

print(reg)
