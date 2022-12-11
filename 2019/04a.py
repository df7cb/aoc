#!/usr/bin/python3

a, b = 347312, 805915

def good(x):
    double = False
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            return False
        if x[i] == x[i+1]:
            double = True
    return double

num = 0
for x in range(a, b+1):
    if good(str(x)):
        num += 1

print(num)
