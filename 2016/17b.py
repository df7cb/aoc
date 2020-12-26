#!/usr/bin/python3

from collections import deque
import hashlib

#passcode = b'hijkl'
#passcode = b'ihgpwlah'
#passcode = b'kglvqrro'
#passcode = b'ulqzkmiv'
passcode = b'vwbaicqe'

x0, y0 = 0, 0

queue = deque([(0, '', x0, y0)]) # round number, path, x, y

def open_doors(path):
    md5 = hashlib.new('md5')
    md5.update(passcode)
    md5.update(str(path).encode('utf-8'))
    hexdgt = md5.hexdigest()

    out = set()
    if hexdgt[0] in 'bcdef':
        out.add('U')
    if hexdgt[1] in 'bcdef':
        out.add('D')
    if hexdgt[2] in 'bcdef':
        out.add('L')
    if hexdgt[3] in 'bcdef':
        out.add('R')
    return out

longest_path = 0
while len(queue) > 0:
    r, path, x, y = queue.popleft()
    doors = open_doors(path)
    #print(r, path, x, y, doors)
    if x == y == 3:
        if len(path) > longest_path:
            print('longest path so far:', r, path)
            longest_path = len(path)
        continue
    for d, dx, dy in (('L', -1, 0), ('R', 1, 0), ('U', 0, -1), ('D', 0, 1)):
        if d not in doors:
            continue
        x2, y2 = x+dx, y+dy
        if x2 < 0 or x2 > 3 or y2 < 0 or y2 > 3:
            continue

        queue.append((r+1, path+d, x2, y2))
