#!/usr/bin/python3

list = []

with open('5.txt') as f:
    for line in f:
        binary = line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0').strip()
        number = int(binary, 2)
        list.append(number)

for i in range(1000):
    if i-1 in list and i not in list and i+1 in list:
        print(i)
