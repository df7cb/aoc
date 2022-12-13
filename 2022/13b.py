#!/usr/bin/python3

from functools import cmp_to_key

def lt(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            if a == b:
                return 0
            else:
                return -1 if a < b else 1
        elif isinstance(b, list):
            return lt([a], b)
    elif isinstance(a, list):
        if isinstance(b, int):
            return lt(a, [b])
        elif isinstance(b, list):
            if a == b == []:
                return 0
            if b == []:
                return 1
            elif a == []:
                return -1
            else:
                first = lt(a[0], b[0])
                if first != 0:
                    return first
                else:
                    return lt(a[1:], b[1:])

    raise Exception('Unknown types')

packets = [[], [2], [6]]

with open("13.txt") as f:
    while True:
        packets.append(eval(f.readline()))
        packets.append(eval(f.readline()))
        if f.readline() == '':
            break

print(packets)
packets.sort(key=cmp_to_key(lt))

for p in packets:
    print(p)

m1 = packets.index([2])
m2 = packets.index([6])
print(m1 * m2)
