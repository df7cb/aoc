#!/usr/bin/python3

count = 0

with open("02.txt") as f:
    line = f.read().strip()
    for rng in line.split(','):
        l, r = rng.split('-')
        print(l, r)
        li, ri = int(l), int(r)
        for i in range(li, ri + 1):
            t = str(i)
            le = len(t)

            for d in range(1, le):
                if le % d == 0:
                    tmp = ''
                    for x in range(le // d):
                        tmp += t[:d]
                    if t == tmp:
                        print(d, t)
                        count += i
                        break

print(count)
