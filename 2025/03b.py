#!/usr/bin/python3

jolts = 0

def check(bank, num):
    #print(num, bank)
    if len(bank) < 12-num:
        return None
    for d in range(9, -1, -1):
        dd = chr(48+d)
        if dd in bank:
            if num == 12:
                return dd
            i = bank.index(dd)
            r = check(bank[i+1:], num+1)
            #print(num, bank, r)
            if r != None:
                return dd + r
    return None

with open("03.txt") as f:
    for bank in f:
        print(bank.strip())
        c = check(bank.strip(), 1)
        print(c)
        jolts += int(c)

print(jolts)
