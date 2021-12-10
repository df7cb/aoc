#!/usr/bin/python3

def parse(s):
    stack = []
    for c in s:
        if c in ('(', '[', '{', '<'):
            stack.append(c)

        elif c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 3
        elif c == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return 57
        elif c == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 1197
        elif c == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                return 25137
        else:
            print("c", c)
            assert(0)

    print("stack", stack)
    return 0

with open('10.txt') as f:
    score = 0
    for line in f:
        score += parse(line.strip())

print(score)
