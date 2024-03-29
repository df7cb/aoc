#!/usr/bin/python3

with open("17.txt") as f:
    city = [line.strip() for line in f]

y, x = 0, 0
queue = {}
seen = {}

def enqueue(queue, seen, key, dist):
    (y, x, tail) = key
    if (y, x) in seen:
        if tail in seen[(y, x)]:
            if dist < seen[(y, x)][tail]:
                seen[(y, x)][tail] = dist
            else:
                return
        else:
            seen[(y, x)][tail] = dist
    else:
        seen[(y, x)] = { tail: dist }

    if key in queue:
        d = queue[key]
        if dist < d:
            queue[key] = dist
    else:
        queue[key] = dist

enqueue(queue, seen, (0, 0, '   '), 0)

count=0
while queue:
    for key in queue:
        (y, x, tail) = key
        dist = queue.pop(key)
        break
    count+=1
    if count%100000 == 0:
        print(len(queue), y, x, dist, tail)

    if x > 0 and tail != '<<<' and tail[-1] != '>':
        enqueue(queue, seen, (y, x-1, tail[1:] + '<'), dist+int(city[y][x-1]))
    if x < len(city[0]) - 1 and tail != '>>>' and tail[-1] != '<':
        enqueue(queue, seen, (y, x+1, tail[1:] + '>'), dist+int(city[y][x+1]))
    if y > 0 and tail != '^^^' and tail[-1] != 'v':
        enqueue(queue, seen, (y-1, x, tail[1:] + '^'), dist+int(city[y-1][x]))
    if y < len(city) - 1 and tail != 'vvv' and tail[-1] != '^':
        enqueue(queue, seen, (y+1, x, tail[1:] + 'v'), dist+int(city[y+1][x]))

ex = seen[(len(city)-1, len(city[0])-1)]
print(ex)
print(min(ex.values()))
