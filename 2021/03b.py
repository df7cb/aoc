#!/usr/bin/python3

data = []

with open('03.txt') as f:
    for line in f:
        bits = [int(x) for x in line.strip()]
        data.append(bits)

def most(data, pos, tie):
    ones, zeros = 0, 0
    for line in data:
        if line[pos]:
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        return 1
    elif ones < zeros:
        return 0
    else:
        return tie

def least(data, pos, tie):
    ones, zeros = 0, 0
    for line in data:
        if line[pos]:
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        return 0
    elif ones < zeros:
        return 1
    else:
        return tie

def filter(data, pos, bit):
    data2 = []
    for line in data:
        if line[pos] == bit:
            data2.append(line)

    return data2

oxygen_data = data
oxygen = 0

for pos in range(len(data[0])):
    m = most(oxygen_data, pos, 1)
    oxygen_data = filter(oxygen_data, pos, m)
    oxygen *= 2
    oxygen += m
    print(m)

print(oxygen_data)
print(oxygen)

co2_data = data

for pos in range(len(data[0])):
    m = least(co2_data, pos, 0)
    co2_data = filter(co2_data, pos, m)
    if len(co2_data) <= 1:
        break
    print(m)

print(co2_data)

co2 = 0
for bit in co2_data[0]:
    co2 *= 2
    co2 += bit
print(co2)

print(oxygen * co2)
