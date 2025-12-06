#!/usr/bin/python3

numbers = []

with open("06.txt") as f:
    for line in f:
        numbers.append(line.strip("\n"))

print(numbers)

def product(l):
    r = 1
    for x in l:
        r *= x
    return r

total = 0
problem = []
for i in range(len(numbers[0]) - 1, -1, -1):
    number = ''.join([numbers[j][i] for j in range(len(numbers)-1)])
    if number.strip() == "": continue
    problem.append(int(number))
    op = numbers[-1][i]
    if op == '+':
        print(problem, op)
        total += sum(problem)
        problem = []
    elif op == '*':
        print(problem, op)
        total += product(problem)
        problem = []

print(total)
