#!/usr/bin/python3

with open("09.txt") as f:
    diskmap = list(f.read().strip())

print(diskmap)

disk = []

id = 0
in_file = True

for x in diskmap:
    disk.append([id if in_file else '.', int(x)])
    if in_file:
        id += 1
    in_file = not in_file

print(disk)

def compact():
    global disk
    for i in range(len(disk)-1, 0, -1):
        block = disk[i]
        if block[0] == '.': continue # won't move free space
        for j in range(i):
            if disk[j][0] != '.': continue
            if disk[j][1] < block[1]: continue # does not fit
            assert(block[0] != '.')
            print("moving", block)

            disk[j][0] = block[0]
            disk[i][0] = '.'
            if disk[j][1] > block[1]:
                disk = disk[:j+1] + [['.', disk[j][1] - block[1]]] + disk[j+1:]
                disk[j][1] = block[1]
                #print(disk)
                return True # indices changed, start over
            #print(disk)
            break
    return False # done

while compact(): pass

print(disk)

checksum = 0
i = 0
for block in disk:
    for x in range(block[1]):
        if block[0] != '.':
            checksum += i * block[0]
        i += 1

print(checksum)
