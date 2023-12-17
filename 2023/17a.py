#!/usr/bin/python3

with open("17.txt") as f:
    city = [line.strip() for line in f]

def add_tail(tail, d):
    if len(tail) == 3:
        return tail[1:] + d
    else:
        return tail + d

y, x = 0, 0
#queue = ((0, 1, city[0][1], ['>']), (1, 0, city[1][0], ['v']))
queue = [(0, 0, 0, '')]
seen = {}

while queue:
    y, x, dist, tail = queue.pop()
    if (y, x) in seen:
        if tail in seen[(y, x)]:
            if dist < seen[(y, x)][tail]:
                seen[(y, x)][tail] = dist
            else:
                continue
        else:
            seen[(y, x)][tail] = dist
    else:
        seen[(y, x)] = { tail: dist }
    print(y, x, dist, tail)

    if x > 0 and tail != '<<<' and (not tail or tail[-1] != '>'):
        queue.append((y, x-1, dist+int(city[y][x-1]), add_tail(tail, '<')))
    if x < len(city[0]) - 1 and tail != '>>>' and (not tail or tail[-1] != '<'):
        queue.append((y, x+1, dist+int(city[y][x+1]), add_tail(tail, '>')))
    if y > 0 and tail != '^^^' and (not tail or tail[-1] != 'v'):
        queue.append((y-1, x, dist+int(city[y-1][x]), add_tail(tail, '^')))
    if y < len(city) - 1 and tail != 'vvv' and (not tail or tail[-1] != '^'):
        queue.append((y+1, x, dist+int(city[y+1][x]), add_tail(tail, 'v')))

