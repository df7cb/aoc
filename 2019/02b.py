#!/usr/bin/python3

with open("02.txt") as f:
    prg0 = [int(x) for x in f.read().split(',')]

def run(noun, verb):
    prg = [x for x in prg0]
    prg[1] = noun
    prg[2] = verb
    pc = 0

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

    return prg[0]

for noun in range(100):
    for verb in range(100):
        res = run(noun, verb)
        print(noun, verb, res)
        if res == 19690720:
            exit()
