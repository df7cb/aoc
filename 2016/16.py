#!/usr/bin/python3

def dragon(a):
    b = a[::-1]
    b = b.replace('0','o').replace('1','0').replace('o','1')
    return a + '0' + b

print(dragon('101'))

def fill(a, size):
    while len(a) < size:
        a = dragon(a)
    return a[:size]

def checksum(a):
    while len(a) % 2 == 0:
        new_a = ''
        for p in range(0, len(a), 2):
            if a[p] == a[p+1]:
                new_a += '1'
            else:
                new_a += '0'
        a = new_a
    return a

# example
d = fill('10000', 20)
c = checksum(d)
print(d, c)

# 16a
d = fill('10011111011011001', 272)
c = checksum(d)
print(d, c)

# 16b
d = fill('10011111011011001', 35651584)
c = checksum(d)
print(c)
