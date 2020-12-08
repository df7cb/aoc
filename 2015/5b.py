#!/usr/bin/python3

count = 0

with open('5.txt') as f:
    for string in f:
        string = string.strip()

        for p in range(len(string) - 2):
            if string.find(string[p:p+2], p+2) >= p+2:
                break
        else:
            print (string, 'is missing pair')
            continue

        for p in range(len(string) - 2):
            if string[p] == string[p+2]:
                break
        else:
            print (string, 'is missing repetition')
            continue

        print (string, 'is good')

        count += 1

print(count)
