#!/usr/bin/python3

count = 0

with open('5.txt') as f:
    for string in f:
        string = string.strip()

        c = 0
        for char in string:
            if char in 'aeiou':
                c += 1
        if c < 3:
            print (string, 'is missing vowels')
            continue

        for p in range(len(string) - 1):
            if string[p] == string[p+1]:
                break
        else:
            print (string, 'is missing duplicates')
            continue

        found = False
        for cc in ['ab', 'cd', 'pq', 'xy']:
            if string.find(cc) >= 0:
                found = True
        if found:
            print (string, 'has bad substring')
            continue

        print (string, 'is good')

        count += 1

print(count)
