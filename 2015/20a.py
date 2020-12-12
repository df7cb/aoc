#!/usr/bin/python3

import math

goal = int(36000000 / 10)

def factors(n):
    f = [1, n]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            f.append(i)
            div = int(n / i)
            if div != i:
                f.append(div)
    return f

def factors_sum(n):
    f = 1 + n # 1 and n
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            f += i
            div = int(n / i)
            if div != i:
                f += div
    return f

i = 0
max_f = 0
while True:
    f = factors_sum(i)
    if f >= max_f:
        print(i, f)
        max_f = f
    if f >= goal:
        break
    #i += 1
    i += 60
