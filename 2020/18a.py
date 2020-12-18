#!/usr/bin/python3

import lark

@lark.v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(lark.Transformer):
    from operator import add, mul
    number = int

    def __init__(self):
        self.vars = {}

parser = lark.Lark('''?expr: "(" expr ")"
                      | expr "+" term -> add
                      | expr "*" term -> mul
                      | NUMBER -> number
                      ?term: "(" expr ")"
                      | NUMBER -> number
                 %import common.NUMBER
                 %import common.WS
                 %ignore WS
         ''', parser='lalr', start='expr', transformer=CalculateTree())

total = 0

with open('18.txt') as f:
    for line in f:
        r = parser.parse(line)
        print(line, '=', r)
        total += r

print(total)
