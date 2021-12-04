#!/usr/bin/python3

r = [3, 7]
e = [0, 1]

#want = [int(x) for x in '51589']
want = [int(x) for x in '704321']
wantlen = len(want)

tick = 0
while True:
    s = r[e[0]] + r[e[1]]
    r.extend([int(x) for x in str(s)])
    for i in (0, 1):
        e[i] = (e[i] + r[e[i]] + 1) % len(r)

    #print(r)

    if r[-wantlen:] == want:
        print(len(r) - wantlen)
        break
    if r[-wantlen-1:-1] == want:
        print(len(r) - wantlen - 1)
        break
