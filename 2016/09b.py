#!/usr/bin/python3

import re

with open('09.txt') as f:
    data = f.read().strip()

def parse(data):
    if m := re.match('\((\d+)x(\d+)\)', data):
        length, repeat = int(m[1]), int(m[2])
        p = len(m[0])
        return repeat * parse (data[p:p+length]) + parse(data[p+length:])
    elif m := re.match('[^\(]+', data):
        p = len(m[0])
        return p + parse(data[p:])
    elif data == '':
        return 0
    else:
        raise SyntaxError(data)

print(data)
print(parse(data))
