#!/usr/bin/python3

import re

def stringsort(str):
    return "".join(sorted(str))

def select_one(l):
    if len(l) != 1:
        print(l)
        assert(len(l) == 1)
    return l[0]

def analyze(inputs):
    one = [x for x in inputs if len(x) == 2][0]
    seven = [x for x in inputs if len(x) == 3][0]
    four = [x for x in inputs if len(x) == 4][0]
    eight = [x for x in inputs if len(x) == 7][0]

    weight_6 = [x for x in inputs if len(x) == 6] # 069
    weight_5 = [x for x in inputs if len(x) == 5] # 235

    # three has all digits from one
    three = select_one([x for x in weight_5 if one[0] in x and one[1] in x])

    # nine has all digits from three
    nine = select_one([x for x in weight_6 if len([y for y in three if y in x]) == 5])

    # zero has all digits from one, but isn't nine
    zero = select_one([x for x in weight_6 if x != nine and one[0] in x and one[1] in x])
    # six is the remaining one with 6 digits
    six = select_one([x for x in weight_6 if x != nine and x != zero])

    # the f digit is in 6 and 1
    digit_f = select_one([x for x in one if x in six])

    # 5 has the f digit and isn't 3
    five = select_one([x for x in weight_5 if digit_f in x and x != three])

    # 2 is the remaining one
    two = select_one([x for x in weight_5 if x != three and x != five])

    digits = {
            zero: 0,
            one: 1,
            two: 2,
            three: 3,
            four: 4,
            five: 5,
            six: 6,
            seven: 7,
            eight: 8,
            nine: 9,
            }
    #print(digits)
    assert(len(digits) == 10)

    return digits

def decode(digits, outputs):
    s = 0
    for out in outputs:
        s *= 10
        s += digits[out]
    return s

with open('08.txt') as f:
    s = 0
    for line in f:
        m = re.match('(.*) \| (.*)', line)
        inputs = [stringsort(x) for x in m.group(1).split(' ')]
        outputs = [stringsort(x) for x in m.group(2).split(' ')]
        digits = analyze(inputs)
        val = decode(digits, outputs)
        print(digits, val)
        s += val

print("Sum is", s)
