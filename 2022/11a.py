#!/usr/bin/python3

import re

monkeys = []

with open("11.txt") as f:
    for line in f:
        if re.match('^Monkey', line):
            monkeys.append({'inspect': 0})
        elif m := re.search('Starting items: (.*)', line):
            monkeys[-1]['items'] = eval(f'[{m.group(1)}]')
        elif m := re.search('Operation: (.*)', line):
            monkeys[-1]['op'] = m.group(1)
        elif m := re.search('Test: divisible by (\d+)', line):
            monkeys[-1]['div'] = int(m.group(1))
        elif m := re.search('(true|false): throw to monkey (\d+)', line):
            monkeys[-1][m.group(1) == 'true'] = int(m.group(2))

print(monkeys)

for turn in range(20):
    for monkey in monkeys:
        print(monkey)
        for old in monkey['items']:
            eval(compile(monkey['op'], '11a.py', 'single'))
            new = new // 3
            next_monkey = monkey[new % monkey['div'] == 0]
            print(old, new, next_monkey)
            monkeys[next_monkey]['items'].append(new)
            monkey['inspect'] += 1
        monkey['items'] = []
    print(monkeys)

inspects = [monkey['inspect'] for monkey in monkeys]
inspects.sort()
print(inspects)
print(inspects[-2] * inspects[-1])
