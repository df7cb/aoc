#!/usr/bin/python3

import re

sum = 0

with open('04.txt') as f:
    for line in f:
        m = re.match('(.*)-(\d+)\[(.*)\]', line)
        name = m[1]
        sector = int(m[2])
        chars = {}
        for c in name:
            if c != '-':
                if c not in chars:
                    chars[c] = 0
                chars[c] += 1
        #print(chars)
        sort = list(chars.keys())
        sort.sort(key=lambda x: (-chars[x], x))
        #print(sort)
        checksum = ''.join(sort)
        #print(m[3], checksum)

        if m[3] == checksum[0:5]:
            sum += sector # part 1

            #print(line)
            decoded = ''
            for c in name:
                if c == '-':
                    decoded += ' '
                else:
                    decoded += chr((ord(c)-97+sector) % 26 + 97)
            print(decoded, sector)
            if 'northpole' in decoded:
                print ('########', decoded, sector)

print(sum) # part 1
