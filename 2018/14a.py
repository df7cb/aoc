#!/usr/bin/python3

r = [3, 7]
e = [0, 1]

#want = 9
want = 704321

tick = 0
while True:
    s = r[e[0]] + r[e[1]]
    r.extend([int(x) for x in str(s)])
    for i in (0, 1):
        e[i] = (e[i] + r[e[i]] + 1) % len(r)

    #print(r)

    if len(r) >= want + 10:
        print(''.join([str(x) for x in r[want:]]))
        break
