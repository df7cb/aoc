#!/usr/bin/python3

import lark

@lark.v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(lark.Transformer):
    from operator import add, mul
    number = int

    def __init__(self):
        self.vars = {}

parser = lark.Lark('''?expr: prod "*" prod -> mul
                      | expr "*" prod -> mul
                      | prod
                      ?prod: term "+" term -> add
                      | prod "+" term -> add
                      | term
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
