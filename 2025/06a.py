#!/usr/bin/python3

numbers = []

with open("06.txt") as f:
    for line in f:
        numbers.append(line.split())

print(numbers)
print(len(numbers))

def product(l):
    r = 1
    for x in l:
        r *= x
    return r

total = 0
for i in range(len(numbers[0])):
    op = numbers[-1][i]
    if op == '+':
        total += sum([int(numbers[r][i]) for r in range(len(numbers)-1)])
    elif op == '*':
        total += product([int(numbers[r][i]) for r in range(len(numbers)-1)])
    else:
        assert(0)

print(total)
