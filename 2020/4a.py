#!/usr/bin/python3

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
            #print(fieldnames, fld)
            #print()
            break
    else:
        print(pp)
        number += 1

print(number)
