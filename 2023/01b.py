#!/usr/bin/python3

numbers = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
    ]

sum = 0

with open("01.txt") as f:
    for line in f:
        oldline = line
        first = None
        last = None

        for i in range(len(line)):
            if line[i] in "0123456789":
                if first is None:
                    first = line[i]
                last = line[i]
            for num, n in numbers:
                if len(line) >= i + len(num):
                    if line[i:i+len(num)] == num:
                        if first is None:
                            first = n
                        last = n

        sum += int(first + last)
        print(f"{oldline} {line.strip()} {first} {last}")

print(sum)
