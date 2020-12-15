#!/usr/bin/python3

import hashlib

puzzle = b'uqwqemis'
i = 0

password = list('________')

while True:
    md5 = hashlib.new('md5')
    md5.update(puzzle)
    md5.update(str(i).encode('utf-8'))
    hexdgt = md5.hexdigest()
    if (hexdgt[0:5] == '00000'):
        print(i, hexdgt)
        if int(hexdgt[5], 16) < 8 and password[int(hexdgt[5], 16)] == '_':
            password[int(hexdgt[5])] = hexdgt[6]
        print(''.join(password))
        if '_' not in password:
            break
    i += 1
