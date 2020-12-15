#!/usr/bin/python3

import hashlib

puzzle = b'uqwqemis'
i = 0

password = ''

while True:
    md5 = hashlib.new('md5')
    md5.update(puzzle)
    md5.update(str(i).encode('utf-8'))
    hexdgt = md5.hexdigest()
    if (hexdgt[0:5] == '00000'):
        print(i, hexdgt)
        password += hexdgt[5]
        if len(password) == 8:
            break
    i += 1

print(password)
