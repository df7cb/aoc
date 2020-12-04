#!/usr/bin/python3

import re

with open('4.txt') as f:
    passports = f.read().split("\n\n")

#print(passports)

fieldlist = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

number = 0

for pp in passports:
    fields = pp.split()
    fieldnames = set(map(lambda x: x.split(":")[0], fields))

    for fld in fieldlist:
        if fld not in fieldnames:
            break
    else:
        for fld in fields:
            key, value = fld.split(":")
            if key == 'byr':
                if int(value) < 1920 or int(value) > 2002:
                    break
            if key == 'iyr':
                if int(value) < 2010 or int(value) > 2020:
                    break
            if key == 'eyr':
                if int(value) < 2020 or int(value) > 2030:
                    break
            if key == 'hgt':
                if m := re.match('(\d+)in$', value):
                    if int(m.group(1)) < 59 or int(m.group(1)) > 76:
                        break
                elif m := re.match('(\d+)cm$', value):
                    if int(m.group(1)) < 150 or int(m.group(1)) > 193:
                        break
                else:
                    break
            if key == 'hcl':
                if not re.match('#[a-f0-9]{6}$', value):
                    break
            if key == 'ecl':
                if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    break
            if key == 'pid':
                if not re.match('[0-9]{9}$', value):
                    break
        else:
            number += 1

print(number)
