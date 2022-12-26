#!/usr/bin/python3

with open("20.txt") as f:
    data = [int(x) for x in f]
orig = [int(x) for x in data]

debug = False

if debug:
    print('Initial arrangement:')
    print(', '.join([str(x) for x in data]))
    print()
print(len(data))
print(min(data))
print(max(data))

for x in orig:
    if x == 0:
        if debug:
            print(f"{x} does not move:")
            print(', '.join([str(x) for x in data]))
            print()
        continue
    pos = data.index(x)
    #if x > 0:
    #    new = (pos+x) % (len(orig)-1)
    #else:
    new = (pos+x-1) % (len(orig)-1) + 1
    if new > pos:
        data = data[:pos] + data[pos+1:new+1] + [x] + data[new+1:]
    else:
        data = data[:new] + [x] + data[new:pos] + data[pos+1:]
    if debug:
        print(f"{x} moves from {pos} to {new}:")
        print(', '.join([str(x) for x in data]))
        print()

zero = data.index(0)
a = data[(zero+1000) % len(orig)]
b = data[(zero+2000) % len(orig)]
c = data[(zero+3000) % len(orig)]
print(a, b, c)
print(a+b+c)
