#!/usr/bin/python3

ones, zeros = [], []

with open('03.txt') as f:
    for line in f:
        line = line.strip()
        if ones == []:
            ones = [0 for x in line]
            zeros = [0 for x in line]
        for pos in range(len(line)):
            bit = int(line[pos])
            if bit:
                ones[pos] += 1
            else:
                zeros[pos] += 1

print(ones)
print(zeros)

gamma, epsilon = 0, 0

for pos in range(len(ones)):
    gamma *= 2
    epsilon *= 2
    if ones[pos] > zeros[pos]:
        gamma += 1
    elif ones[pos] < zeros[pos]:
        epsilon += 1
    else:
        print("uh-oh")

print(gamma, epsilon, gamma * epsilon)
