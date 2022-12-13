#!/usr/bin/python3

def lt(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            if a == b:
                return None
            else:
                return a < b
        elif isinstance(b, list):
            return lt([a], b)
    elif isinstance(a, list):
        if isinstance(b, int):
            return lt(a, [b])
        elif isinstance(b, list):
            if a == []:
                return b != []
            elif b == []:
                return False
            else:
                first = lt(a[0], b[0])
                if first != None:
                    return first
                else:
                    return lt(a[1:], b[1:])

    raise Exception('Unknown types')

pairs = []

with open("13.txt") as f:
    while True:
        left = eval(f.readline())
        right = eval(f.readline())
        pairs.append((left, right))
        if f.readline() == '':
            break

sm = 0
for i in range(1, len(pairs)):
    is_lt = lt(*pairs[i])
    print(*pairs[i], is_lt)
    if is_lt:
        sm += i

print(sm)
