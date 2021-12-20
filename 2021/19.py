#!/usr/bin/python3

import re
from itertools import permutations

scanner_view = {}
scanner_pos = { 0: (0, 0, 0) }

threshold = 12

with open('19.txt') as f:
    for line in f:
        if m := re.match('--- scanner (\d+) ---', line):
            scanner_number = int(m.group(1))
            scanner_view[scanner_number] = []
        elif line == '\n':
            pass
        else:
            m = re.match('([\d-]+),([\d-]+),([\d-]+)', line)
            scanner_view[scanner_number].append((int(m.group(1)), int(m.group(2)), int(m.group(3))))

# base our world view on scanner 0
beacons = {x:1 for x in scanner_view[0]}
del scanner_view[0]

print(len(beacons), beacons)

def check_align(beacons, view, p, dx, dy, dz, rx, ry, rz):
    count = 0
    for v in view:
        if (rx * v[p[0]] + dx, ry * v[p[1]] + dy, rz * v[p[2]] + dz) in beacons:
            count += 1
    return count

last_scanner_found = 0
def try_align():
    global last_scanner_found
    scanners = scanner_view.keys()
    scanners = [x for x in scanners if x >= last_scanner_found] + [x for x in scanners if x < last_scanner_found]
    for s in scanners:
        print("Trying to align scanner", s)
        for v in scanner_view[s]:
            for b in beacons:
                #print("Trying to align scanner", s, ":", v, "with beacon", b)
                for p in permutations([0, 1, 2]):
                    for rx in (1, -1):
                        for ry in (1, -1):
                            for rz in (1, -1):
                                #if rx+ry+rz not in (3, -1): # skip mirrored alignments
                                #    continue
                                dx = b[0] - rx * v[p[0]]
                                dy = b[1] - ry * v[p[1]]
                                dz = b[2] - rz * v[p[2]]
                                #print("Trying to align scanner", s, ":", v, "with beacon", b, p, rx, ry, rz)
                                count = check_align(beacons, scanner_view[s], p, dx, dy, dz, rx, ry, rz)

                                if count >= threshold:
                                    print("Found match for scanner", s, "at", p, dx, dy, dz, rx, ry, rz)
                                    for v in scanner_view[s]:
                                        coords = (rx * v[p[0]] + dx, ry * v[p[1]] + dy, rz * v[p[2]] + dz)
                                        if coords not in beacons:
                                            print("Found new beacon at", coords)
                                            beacons[coords] = 1
                                    del scanner_view[s]
                                    scanner_pos[s] = (dx, dy, dz)
                                    last_scanner_found = s
                                    print("Scanners left:", scanner_view.keys())
                                    print("Beacons located:", len(beacons))
                                    return True
    return False

while try_align():
    pass

manhattan = 0
for s1 in scanner_pos.values():
    for s2 in scanner_pos.values():
        if s1 == s2:
            continue
        manhattan = max(manhattan, abs(s1[0]-s2[0]) + abs(s1[1]-s2[1]) + abs(s1[2]-s2[2]))
print("Max Manhattan distance:", manhattan)
