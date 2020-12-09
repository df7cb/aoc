#!/usr/bin/python3

import re

number = '1321131112'
print(number)

def look_and_see(num):
    out = ''
    c0 = None
    n = 0
    for c in num:
        if c0 is None:
            c0 = c
        else:
            if c0 != c:
                out += str(n) + c0
                n = 0
                c0 = c
        n += 1
    if c0 is not None:
        out += str(n) + c0
    return out

for x in range(50):
    number = look_and_see(number)

print(len(number))
