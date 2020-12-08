#!/usr/bin/python3

import hashlib

puzzle = b'ckczppom'
i = 0


while True:
    md5 = hashlib.new('md5')
    md5.update(puzzle)
    md5.update(str(i).encode('utf-8'))
    hexdgt = md5.hexdigest()
    if i % 10000 == 0:
        print(i, hexdgt)
    if (hexdgt[0:6] == '000000'):
        print(i, hexdgt)
        exit(0)
    i += 1
