#!/usr/bin/python3

import re

def claw(ax, ay, bx, by, x, y):
    print(ax, ay, bx, by, x, y)
    for a in range(101):
        x0 = a * ax
        b = (x - x0) / bx
        if b != int(b): continue
        if b > 100: continue
        print(f"X {x} = {a} * {ax} + {b} + {bx}")
        if a * ay + b * by != y: continue
        print(f"Y {y} = {a} * {ay} + {b} + {by} ***")
        return 3*a + int(b)
    return 0

presses = 0

with open("13.txt") as f:
    while True:
        a = re.match(r'Button A: X\+(\d+), Y\+(\d+)', f.readline())
        if not a: break
        b = re.match(r'Button B: X\+(\d+), Y\+(\d+)', f.readline())
        p = re.match(r'Prize: X=(\d+), Y=(\d+)', f.readline())
        presses += claw(int(a.group(1)), int(a.group(2)), int(b.group(1)), int(b.group(2)), int(p.group(1)), int(p.group(2)))
        f.readline()

print(presses)
