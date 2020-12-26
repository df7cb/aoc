#!/usr/bin/python3

import hashlib
import re

#puzzle = 'abc'
puzzle = 'zpqevtbw'
i = 0
queue = []
keys = []

def stretched_hash(txt):
    for i in range(2016+1):
        md5 = hashlib.new('md5')
        md5.update(txt.encode('utf-8'))
        txt = md5.hexdigest()
    return txt

while True:
    hexdgt = stretched_hash(puzzle + str(i))

    if m := re.search('(\\w)\\1\\1', hexdgt):
        print(i, hexdgt, m[1])

        for i0, m0, h0 in queue:
            if i0 < i-1000:
                queue.remove((i0, m0, h0))
            elif m0*5 in hexdgt:
                print(i, i0, hexdgt, 'found key', h0, m0)
                keys.append(hexdgt)
                if len(keys) >= 64:
                    print('64 keys found in iteration', i, i0)
                    exit(0)

        queue.append((i, m[1], hexdgt))

    i += 1
