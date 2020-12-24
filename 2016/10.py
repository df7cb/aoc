#!/usr/bin/python3

import re

bots = {}
outputs = {}
inputs = []

class bot():
    def __init__(self, number, low_kind, low, high_kind, high):
        self.number = number
        self.low_kind = low_kind
        self.low = low
        self.high_kind = high_kind
        self.high = high
        self.data = []

    def add(self, value):
        print("Bot", self.number, "received", value)
        self.data.append(value)
        if len(self.data) > 2:
            raise Exception('too much input data for bot ' + self.number)
        if len(self.data) == 2:
            self.data.sort()

            if self.data == [17, 61]:
                print('10a:', self.number)

            if self.low_kind == 'output':
                print('Output', self.low, 'is', self.data[0])
                outputs[self.low] = self.data[0]
            else:
                bots[self.low].add(self.data[0])

            if self.high_kind == 'output':
                print('Output', self.high, 'is', self.data[1])
                outputs[self.high] = self.data[1]
            else:
                bots[self.high].add(self.data[1])

with open('10.txt') as f:
    for line in f:
        if m := re.match('bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', line):
            if int(m[1]) in bots:
                raise Exception(m[1] + ' seen before')
            bots[int(m[1])] = bot(int(m[1]), m[2], int(m[3]), m[4], int(m[5]))

        elif m := re.match('value (\d+) goes to bot (\d+)', line):
            inputs.append((int(m[1]), int(m[2])))

        else:
            raise SyntaxError(line)

for val, b in inputs:
    print('Feeding input', val, 'to bot', b)
    bots[b].add(val)

print()

for out in sorted(outputs):
    print('Output', out, 'is', outputs[out])

print()
print('10b:', outputs[0] * outputs[1] * outputs[2])
