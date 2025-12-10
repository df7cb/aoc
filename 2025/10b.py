#!/usr/bin/python3

import re
from sympy import Symbol, Matrix, solve_linear_system, Eq, solve, solve_undetermined_coeffs
variables =          []
for x in range(97, 115):
    variables.append(Symbol(chr(x), positive=True, integer=True))

all_buttons = []
all_joltages = []

with open("10.txt") as f:
    for line in f:
        all_buttons.append([])
        for m in re.findall(r"(?<=\()([\d,]+)(?=\))", line):
            all_buttons[-1].append(tuple([int(x) for x in m.split(',')]))

        m = re.search(r"\{([\d,]+)\}", line)
        all_joltages.append(tuple([int(x) for x in m.group(1).split(',')]))

#print(all_buttons)
#print(all_joltages)

def guess(i, n):
    if i == 0:
        return
    elif i == 1:
        for x in range(n+1):
            yield [x]
    elif i == 2:
        for x in range(n+1):
            for y in range(n+1):
                yield [x, y]
    elif i == 3:
        for x in range(n+1):
            for y in range(n+1):
                for z in range(n+1):
                    yield [x, y, z]
    else:
        assert(0)

total = 0
max_missing = 0

for num in range(len(all_joltages)):
    buttons, joltage = all_buttons[num], all_joltages[num]
    print(num, buttons, joltage)

    matrix = [[0 for x in buttons]+[y] for y in joltage]
    for bi in range(len(buttons)):
        button = buttons[bi]
        for bj in range(len(button)):
            matrix[button[bj]][bi] = 1

    system = Matrix(matrix)
    print(num, system)
    x = solve_linear_system(system, *variables[:len(buttons)], particular=True, quick=True)
    print("solution", x)
    presses = sum(x.values())

    missings = []
    for var in variables[:len(buttons)]:
        if var not in x:
            missings.append(var)
            presses += var
    print("presses", presses)

    print("missing", missings)

    best_presses = presses if missings == [] else None
    max_jolt = max(joltage)
    for g in guess(len(missings), max_jolt):
        ok = True
        for v in x:
            if type(x[v]) == int:
                continue
            r = x[v].subs(zip(missings, g))
            if r < 0 or r != int(r):
                ok = False
                break
        if not ok:
            continue
        p = presses.subs(zip(missings, g))
        if best_presses is None or p < best_presses:
            best_presses = p

    print(num, best_presses)
    total += best_presses

print(total)
