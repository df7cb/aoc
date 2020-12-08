#!/usr/bin/python3

import hashlib

puzzle = b'ckczppom'
i = 0


while True:
    md5 = hashlib.new('md5')
    md5.update(puzzle)
    md5.update(str(i).encode('utf-8'))
    hexdgt = md5.hexdigest()
    print(i, hexdgt)
    if (hexdgt[0:5] == '00000'):
        exit(0)
    i += 1
