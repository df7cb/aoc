#!/usr/bin/python3

def analyze_v(p, s):
    lx = len(p[0])
    ly = len(p)
    w = min(s, lx - s)
    for y in range(ly):
        for dx in range(w):
            if p[y][s - dx - 1] != p[y][s + dx]:
                return False
    return True

def analyze_h(p, s):
    lx = len(p[0])
    ly = len(p)
    w = min(s, ly - s)
    for x in range(lx):
        for dy in range(w):
            if p[s - dy - 1][x] != p[s + dy][x]:
                return False
    return True

def analyze(p):
    lx = len(p[0])
    ly = len(p)
    # vertical mirror:
    for s in range(1, lx): # split
        if analyze_v(p, s):
            return s
    # horizontal mirror:
    for s in range(1, ly): # split
        if analyze_h(p, s):
            return 100 * s

    assert(0)

count = 0

with open("13.txt") as f:
    pattern = []
    for line in f:
        if line.strip():
            pattern.append(line.strip())
        else:
            count += analyze(pattern)
            pattern = []
    count += analyze(pattern)

print(count)
