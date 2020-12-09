#!/usr/bin/python3

code = 0
chars = 0
encoded = 0

with open('8.txt') as f:
    for line in f:
        code += len(line.strip())

        n = 2
        for c in line.strip():
            if c == '"' or c == '\\':
                n += 2
            else:
                n += 1
        encoded += n

print(code, encoded, encoded - code)
