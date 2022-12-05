#!/usr/bin/python3

import re

stacks = [['']]
stacks.append(list('RGJBTVZ'))
stacks.append(list('JRVL'))
stacks.append(list('SQF'))
stacks.append(list('ZHNLFVQG'))
stacks.append(list('RQTJCSMW'))
stacks.append(list('SWTCHF'))
stacks.append(list('DZCVFNJ'))
stacks.append(list('LGZDWRFQ'))
stacks.append(list('JBWVP'))

#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 

#stacks = [['']]
#stacks.append(list('ZN'))
#stacks.append(list('MCD'))
#stacks.append(list('P'))

print(stacks)

with open("05.txt") as f:
     for line in f:
         if m := re.match('move (\d+) from (\d+) to (\d+)', line):
             num = int(m.group(1))
             frm = int(m.group(2))
             to = int(m.group(3))
             print(num, frm, to)
             stacks[to] += reversed(stacks[frm][-num:])
             stacks[frm] = stacks[frm][:-num]
             print(stacks)

for s in stacks:
    print(s[-1], end='')
print()
