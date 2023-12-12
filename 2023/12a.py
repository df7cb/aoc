#!/usr/bin/python3

def consistent(springs, head):
    if len(head) > len(springs):
        return False
    for i in range(len(head)):
        if springs[i] == '?':
            continue
        if springs[i] != head[i]:
            return False
    return True

def check(springs, head, counts):
    if not consistent(springs, head):
        return 0
    print(springs, head, counts)

    count = 0
    if len(head) < len(springs):
        count += check(springs, head + '.', counts)
    if len(counts) > 0 and (len(head) == 0 or head[-1] == '.') and len(head) + counts[0] <= len(springs):
        count += check(springs, head + '#' * counts[0], counts[1:])
    if len(counts) == 0 and len(springs) == len(head):
        return count + 1
    return count

arrangements = 0

with open("12.txt") as f:
    for line in f:
        springs, counts = line.split()
        counts = [int(x) for x in counts.split(',')]
        a = check(springs, '', counts)
        arrangements += a

print(arrangements)
