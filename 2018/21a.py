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

program = []

with open('21.txt') as f:
    m = re.match('#ip (\d)', f.readline())
    ipreg = int(m.group(1))

    for line in f:
        m = re.match('(\S+) (\d+) (\d+) (\d+)', line)
        program.append((m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))))

print(ipreg)
print(program)

def run(r0):
    reg = [0 for x in range(6)]
    reg[0] = r0

    step = 0
    ip_18 = 0
    while True:
        ip = reg[ipreg]
        if ip == 18:
            ip_18 += 1
            if ip_18 >= 100:
                exit(1)
                return False, step
        try:
            cmd = program[ip]
        except:
            return True, step
        op(reg, *cmd)
        #if True or step % 10000 == 0:
        print(step, ip, cmd, reg)
        step += 1
        reg[ipreg] += 1

r0 = 0
while True:
    #print("r0", r0)
    terminated, step = run(r0)
    #if terminated:
    print(r0, terminated, step)
    r0 += 1
