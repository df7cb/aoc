#!/usr/bin/python3

import re

rule = {}

def parse(token):
    if m := re.fullmatch('(\d+) (\d+) \| (\d+) (\d+)', token):
        return '(' + parse(rule[m[1]]) + parse(rule[m[2]]) + '|' + parse(rule[m[3]]) + parse(rule[m[4]]) + ')'
    elif m := re.fullmatch('(\d+) \| (\d+)', token):
        return '(' + parse(rule[m[1]]) + '|' + parse(rule[m[2]]) + ')'
    elif m := re.fullmatch('(\d+) (\d+) (\d+)', token):
        return parse(rule[m[1]]) + parse(rule[m[2]]) + parse(rule[m[3]])
    elif m := re.fullmatch('(\d+) (\d+)', token):
        return parse(rule[m[1]]) + parse(rule[m[2]])
    elif m := re.fullmatch('(\d+)', token):
        return parse(rule[m[1]])
    elif m := re.fullmatch('"(.*)"', token):
        return m[1]
    else:
        raise SyntaxError(token)

total = 0
with open('19.txt') as f:
    for line in f:
        if m := re.match('(\d+): (.*)', line):
            rule[m[1]] = m[2]

        elif line == "\n":
            print(rule)
            regexp = parse(rule["0"])
            print(regexp)
            r = re.compile(regexp)

        else:
            if r.fullmatch(line.strip()):
                print(line.strip())
                total += 1

print(total)
