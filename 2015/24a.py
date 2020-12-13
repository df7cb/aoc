#!/usr/bin/python3

import functools

with open('24.txt') as f:
    packages = [int(line) for line in f.readlines()]

total = sum(packages)
compartment = int(total/3)

print(packages, total, compartment)

def product(l):
    return functools.reduce(lambda a, b: a*b, l)

# compute the minimal number of packages in the first compartment so we can
# restrict the full pass to these partitions
def load1_len(bestc1len, c1, loading, p):
    for p in range(p, len(packages)):
        if loading + packages[p] < compartment:
            bestc1len = load1_len(bestc1len, c1 + [packages[p]], loading + packages[p], p+1)
        elif loading + packages[p] == compartment:
            if len(c1 + [packages[p]]) < bestc1len:
                bestc1len = len(c1 + [packages[p]])
        else:
            break
    return bestc1len

# run through all partitions with length(c1) == bestc1len
def load1(bestc1len, c1, loading, p):
    if len(c1) >= bestc1len:
        return
    for p in range(p, len(packages)):
        if loading + packages[p] < compartment:
            for c11 in load1(bestc1len, c1 + [packages[p]], loading + packages[p], p+1):
                yield c11
        elif loading + packages[p] == compartment:
            if load2(c1 + [packages[p]], [], 0, 0):
                #print(c1 + [packages[p]])
                yield c1 + [packages[p]]
        else:
            break

# check if a c2/c3 partition with a given c1 exists
def load2(c1, c2, loading, p):
    for p in range(p, len(packages)):
        if packages[p] in c1:
            continue
        if loading + packages[p] < compartment:
            if load2(c1, c2 + [packages[p]], loading + packages[p], p+1):
                return True
        elif loading + packages[p] == compartment:
            print(c1, c2 + [packages[p]])
            return True
        else:
            break
    return False

bestc1len = load1_len(len(packages), [], 0, 0)
#bestc1len = 6
print('minimum number of packages in 1st compartment is', bestc1len)
bestquantum = product(packages)
for c1 in load1(bestc1len, [], 0, 0):
    if product(c1) < bestquantum:
        bestquantum = product(c1)
        print(c1, bestquantum)
print(bestquantum)
