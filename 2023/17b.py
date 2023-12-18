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

enqueue(queue, seen, (0, 0, '>'), 0)
enqueue(queue, seen, (0, 0, 'v'), 0)

count=0
while queue:
    for key in queue:
        (y, x, tail) = key
        dist = queue.pop(key)
        break
    count+=1
    if count%100000 == 0:
        print(len(queue), y, x, dist, tail)

    if tail[-1] in ('v', '^'):
        for n in range(4, 11):
            if x-n >= 0:
                enqueue(queue, seen, (y, x-n, '<'), dist+sum(int(city[y][x-i]) for i in range(1, n+1)))
            if x+n < len(city[0]):
                enqueue(queue, seen, (y, x+n, '<'), dist+sum(int(city[y][x+i]) for i in range(1, n+1)))
    if tail[-1] in ('<', '>'):
        for n in range(4, 11):
            if y-n >= 0:
                enqueue(queue, seen, (y-n, x, '^'), dist+sum(int(city[y-i][x]) for i in range(1, n+1)))
            if y+n < len(city):
                enqueue(queue, seen, (y+n, x, '^'), dist+sum(int(city[y+i][x]) for i in range(1, n+1)))

ex = seen[(len(city)-1, len(city[0])-1)]
print(ex)
print(min(ex.values()))
