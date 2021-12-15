#!/usr/bin/python3

import re

def op(reg, code, a, b, c):
    if code == 'addr': # (add register) stores into register C the result of adding register A and register B.
        res = reg[a] + reg[b]
    elif code == 'addi': # (add immediate) stores into register C the result of adding register A and value B.
        res = reg[a] + b
    elif code == 'mulr': # (multiply register) stores into register C the result of multiplying register A and register B.
        res = reg[a] * reg[b]
    elif code == 'muli': # (multiply immediate) stores into register C the result of multiplying register A and value B.
        res = reg[a] * b
    elif code == 'banr': # (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
        res = reg[a] & reg[b]
    elif code == 'bani': # (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
        res = reg[a] & b
    elif code == 'borr': # (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
        res = reg[a] | reg[b]
    elif code == 'bori': # (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
        res = reg[a] | b
    elif code == 'setr': # (set register) copies the contents of register A into register C. (Input B is ignored.)
        res = reg[a]
    elif code == 'seti': # (set immediate) stores value A into register C. (Input B is ignored.)
        res = a
    elif code == 'gtir': # (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
        res = a > reg[b]
    elif code == 'gtri': # (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
        res = reg[a] > b
    elif code == 'gtrr': # (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
        res = reg[a] > reg[b]
    elif code == 'eqir': # (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
        res = a == reg[b]
    elif code == 'eqri': # (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
        res = reg[a] == b
    elif code == 'eqrr': # (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
        res = reg[a] == reg[b]

    reg[c] = int(res)

reg = [0 for x in range(6)]
reg[0] = 1

program = []

with open('19.txt') as f:
    m = re.match('#ip (\d)', f.readline())
    ipreg = int(m.group(1))

    for line in f:
        m = re.match('(\S+) (\d+) (\d+) (\d+)', line)
        program.append((m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))))

#print(ipreg)
#print(program)

step = 0
expect = None
while True:
    ip = reg[ipreg]
    try:
        cmd = program[ip]
    except:
        break
    #if ip in (3, 12):
    #    print('Before:', step, ip, cmd, reg)
    if ip == 12 and expect is not None:
        if reg != expect:
            print("Reg is:", reg)
            print("Expect:", expect)
            exit(0)
            expect = None

    # Hack for part 2:
    # Before: 35713  3 ('mulr', 5, 3, 4) [7, 892,  3,   1, 0, 6]   transform this
    # ...
    # Before: 42848 12 ('addi', 5, 1, 5) [7, 892, 12, 893, 1, 6] ... into this
    if ip == 3:
        #print("Hack!")
        r0 = reg[0]
        if reg[1] % reg[5] == 0 and reg[3] <= reg[1]//reg[5] <= reg[1]:
            r0 += reg[5]
        expect = [r0, reg[1], 12, reg[1]+1, 1, reg[5]]
        reg[0] = r0
        reg[ipreg] = 12
        reg[3] = reg[1] + 1
        reg[4] = 1
        continue
    op(reg, *cmd)
    #print(step, ip, cmd, reg)
    if step % 100000 == 0:
        print('After: ', step, ip, cmd, reg)
    step += 1
    reg[ipreg] += 1

print(step, ip, cmd, reg)
