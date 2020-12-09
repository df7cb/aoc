#!/usr/bin/python3

code = 0
chars = 0

with open('8.txt') as f:
    for line in f:
        code += len(line.strip())
        m = eval(line)
        chars += len(m)
print(code, chars, code - chars)
