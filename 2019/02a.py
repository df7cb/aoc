#!/usr/bin/python3

pc = 0
with open("02.txt") as f:
    prg = [int(x) for x in f.read().split(',')]

print(prg)

prg[1] = 12
prg[2] = 2

while True:
    op = prg[pc]
    assert op in (1, 2, 99)
    if op == 1:
        prg[prg[pc+3]] = prg[prg[pc+1]] + prg[prg[pc+2]]
    elif op == 2:
        prg[prg[pc+3]] = prg[prg[pc+1]] * prg[prg[pc+2]]
    elif op == 99:
        break
    pc += 4

print(prg)
print(prg[0])
