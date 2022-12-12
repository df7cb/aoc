#!/usr/bin/python3

with open("05.txt") as f:
    prg = [int(x) for x in f.read().split(',')]

def run(prg, noun=None, verb=None):
    if noun:
        prg[1] = noun
    if verb:
        prg[2] = verb
    pc = 0

    while True:
        assert prg[pc] >= 0
        op = prg[pc] % 100;
        im1 = (prg[pc] // 100) % 10;
        im2 = (prg[pc] // 1000) % 10;
        im3 = (prg[pc] // 10000) % 10;

        if op == 1:
            prg[prg[pc+3]] = (prg[pc+1] if im1 else prg[prg[pc+1]]) + \
                             (prg[pc+2] if im2 else prg[prg[pc+2]])
            pc += 4

        elif op == 2:
            prg[prg[pc+3]] = (prg[pc+1] if im1 else prg[prg[pc+1]]) * \
                             (prg[pc+2] if im2 else prg[prg[pc+2]])
            pc += 4

        elif op == 3:
            prg[prg[pc+1]] = int(input('> '))
            pc += 2

        elif op == 4:
            print(prg[pc+1] if im1 else prg[prg[pc+1]])
            pc += 2

        elif op == 99:
            break

        else:
            raise Exception(f'invalid opcode {prg[pc]} pc={pc}')

    return prg[0]

run(prg)
