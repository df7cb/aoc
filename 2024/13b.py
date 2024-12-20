#!/usr/bin/python3

import re
from fractions import Fraction

def claw(ax, ay, bx, by, x, y):
    a = Fraction(x * by - y * bx, ax * by - ay * bx)
    b = Fraction(ax * y - ay * x, ax * by - ay * bx)
    if a.denominator != 1 or b.denominator != 1: return 0
    print(ax, ay, bx, by, x, y, a, b)
    print(a * ax + b * bx, x)
    print(a * ay + b * by, y)
    assert(a * ax + b * bx == x)
    assert(a * ay + b * by == y)
    return int(3*a + b)

presses = 0

with open("13.txt") as f:
    while True:
        a = re.match(r'Button A: X\+(\d+), Y\+(\d+)', f.readline())
        if not a: break
        b = re.match(r'Button B: X\+(\d+), Y\+(\d+)', f.readline())
        p = re.match(r'Prize: X=(\d+), Y=(\d+)', f.readline())
        presses += claw(int(a.group(1)), int(a.group(2)), int(b.group(1)), int(b.group(2)), 10000000000000 + int(p.group(1)), 10000000000000 + int(p.group(2)))
        f.readline()

print(presses)
