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
    #print(springs, head, counts)

    count = 0
    lh = len(head)
    ls = len(springs)
    lc = len(counts)
    if lh < ls:
        count += check(springs, head + '.', counts)
    if lc > 0 and (lh == 0 or head[-1] == '.') and lh + sum(counts) + lc - 1 <= ls:
        count += check(springs, head + '#' * counts[0], counts[1:])
    if lc == 0 and ls == lh:
        if count % 10000 == 1:
            print(head, count)
        return count + 1
    return count

arrangements = 0

with open("12.txt") as f:
    for line in f:
        springs, counts = line.split()
        springs = (springs + '?') * 4 + springs
        counts = [int(x) for x in counts.split(',')]
        counts = counts * 5
        print(springs, counts)
        a = check(springs, '', counts)
        arrangements += a
        print(springs, counts, a, arrangements)

print(arrangements)
