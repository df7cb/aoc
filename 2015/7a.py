#!/usr/bin/python3

import re
import types

wire = {}
wire_cache = {}

with open('7.txt') as f:
    for line in f:
        m = re.match('(.*) -> (.*)', line)
        wire[m[2]] = m[1]

def value(w):
    if w in wire_cache:
        return wire_cache[w]

    if m := re.fullmatch('\d+', w):
        ret = int(w) # convert to int
    elif m := re.fullmatch('NOT (.*)', w):
        ret = (~ value(m[1])) & 0xffff;
    elif m := re.fullmatch('(.*) AND (.*)', w):
        ret = value(m[1]) & value(m[2])
    elif m := re.fullmatch('(.*) OR (.*)', w):
        ret = value(m[1]) | value(m[2])
    elif m := re.fullmatch('(.*) LSHIFT (.*)', w):
        ret = (value(m[1]) << value(m[2])) & 0xffff;
    elif m := re.fullmatch('(.*) RSHIFT (.*)', w):
        ret = value(m[1]) >> value(m[2])
    else:
        ret = value(wire[w]) # single wire name

    wire_cache[w] = ret
    return ret

print(value('a'))
