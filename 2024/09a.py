#!/usr/bin/python3

with open("09.txt") as f:
    diskmap = list(f.read().strip())

print(diskmap)

disk = []

id = 0
in_file = True

for x in diskmap:
    for i in range(int(x)):
        disk.append(id if in_file else '.')
    if in_file:
        id += 1
    in_file = not in_file

print(disk)

for i in range(len(disk)):
    if disk[i] == '.':
        free = i
        break

assert(free >= 0)
print(free)

i = len(disk) - 1
while i >= free:
    disk[free] = disk[i]
    disk[i] = '.'
    while disk[free] != '.': free += 1
    while disk[i] == '.': i -= 1

print(disk)

checksum = 0
for i in range(len(disk)):
    if disk[i] != '.':
        checksum += i * int(disk[i])
print(checksum)
