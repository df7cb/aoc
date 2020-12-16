#!/usr/bin/python3

import re

fields = {}
valid_numbers = set()
error_rate = 0
my_ticket = None
valid_tickets = []

with open('16.txt') as f:
    for line in f:
        if m := re.match('(.*): (\d+)-(\d+) or (\d+)-(\d+)', line):
            fields[m[1]] = set()
            for x in list(range(int(m[2]), int(m[3])+1)) + list(range(int(m[4]), int(m[5])+1)):
                valid_numbers.add(x)
                fields[m[1]].add(x)

        elif ',' in line:
            if my_ticket is None:
                my_ticket = [int(x) for x in line.split(',')]
                continue

            for i in [int(x) for x in line.split(',')]:
                if i not in valid_numbers:
                    error_rate += i
                    break
            else:
                valid_tickets.append([int(x) for x in line.split(',')])

print('error rate (16a)', error_rate)
print(my_ticket)

fieldnames = set(fields.keys())
columns = set(range(len(my_ticket)))
validated_fields = {}

while len(columns) > 0:
    for f in fieldnames:
        column_candidates = set()
        for c in columns:
            for r in range(len(valid_tickets)):
                if valid_tickets[r][c] not in fields[f]:
                    break
            else:
                #print('column', c, 'is valid for', f)
                column_candidates.add(c)
        if len(column_candidates) == 1:
            c = column_candidates.pop()
            validated_fields[f] = c
            columns.remove(c)

print('fields:', validated_fields)

result = 1
for f in [x for x in fields if 'departure' in x]:
    ticket_field = my_ticket[validated_fields[f]]
    print(f, ticket_field)
    result *= ticket_field
print('16b:', result)
