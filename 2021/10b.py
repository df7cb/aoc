#!/usr/bin/python3

def value(stack):
    score = 0
    print("stack", stack)
    if stack is None:
        return 0
    stack.reverse()
    for c in stack:
        score *= 5
        if c == '(':
            score += 1
        elif c == '[':
            score += 2
        elif c == '{':
            score += 3
        elif c == '<':
            score += 4
    return score

def parse(s):
    stack = []
    for c in s:
        if c in ('(', '[', '{', '<'):
            stack.append(c)

        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return 0
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 0
        elif c == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                return 0
        else:
            print("c", c)
            assert(0)

    return value(stack)

with open('10.txt') as f:
    score = []
    for line in f:
        v = parse(line.strip())
        if v > 0:
            score.append(v)

def median(l):
    l.sort()
    return l[len(l)//2]

print(score)
print(median(score))
