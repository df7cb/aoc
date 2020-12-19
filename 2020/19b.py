#!/usr/bin/python3

import lark
import re

parser = lark.Lark('''
p44: p91 p71
| p77 p109
p94: p15 p77
| p129 p91
p73: p113 p77
| p24 p91
p125: p77 p38
| p91 p37
p25: p77 p24
| p91 p112
p37: p105 p77
| p50 p91
p47: p22 p91
| p105 p77
p67: p91 p109
| p77 p45
p130: p58 p91
| p6 p77
p2: p19 p77
| p10 p91
p48: p77 p76
| p91 p7
p20: p10 p91
| p65 p77
p65: p22 p77
| p115 p91
p29: p77 p126
| p91 p79
p105: p77 p91
| p91 p91
p102: p87 p77
| p114 p91
p38: p50 p77
| p50 p91
p56: p91 p107
| p77 p106
p9: p77 p101
| p91 p73
p21: p77 p72
| p91 p54
p35: p22 p77
| p112 p91
p101: p91 p115
| p77 p34
p122: p77 p105
| p91 p14
p108: p77 p111
| p91 p52
p66: p3 p91
| p27 p77
p112: p91 p28
| p77 p91
p61: p91 p24
| p77 p34
p77: "a"
p64: p77 p99
| p91 p119
p106: p77 p68
| p91 p22
p107: p24 p77
| p113 p91
p39: p91 p22
p31: p53 p91
| p127 p77
// p8: p42
p8: p42 | p42 p8
p88: p34 p91
| p113 p77
p27: p49 p91
| p25 p77
p99: p91 p87
| p77 p58
p10: p77 p113
| p91 p50
p123: p91 p100
| p77 p68
p1: p14 p91
| p50 p77
p51: p112 p91
| p34 p77
p42: p77 p36
| p91 p69
p0: p8 p11
p76: p77 p130
| p91 p63
p110: p91 p100
| p77 p124
p46: p91 p15
| p77 p35
p95: p120 p91
| p23 p77
p50: p91 p91
p41: p28 p4
p57: p91 p50
| p77 p115
p72: p91 p46
| p77 p125
p30: p91 p116
| p77 p128
p24: p28 p77
| p91 p91
p109: p77 p24
| p91 p115
p85: p91 p113
| p77 p68
p87: p14 p91
p22: p91 p77
p45: p91 p84
| p77 p113
p18: p77 p12
| p91 p20
p98: p77 p110
| p91 p96
p53: p77 p92
| p91 p90
p120: p77 p68
| p91 p105
p93: p77 p115
| p91 p34
p126: p43 p77
| p118 p91
p79: p77 p47
| p91 p83
p89: p106 p91
| p51 p77
p4: p68 p91
| p105 p77
p62: p77 p33
| p91 p44
p23: p91 p115
| p77 p113
p32: p91 p40
| p77 p39
p54: p59 p91
| p74 p77
p52: p91 p75
| p77 p5
p75: p77 p104
| p91 p15
p104: p22 p91
| p68 p77
p91: "b"
// p11: p42 p31
p11: p42 p31 | p42 p11 p31
p90: p91 p82
| p77 p26
p111: p117 p91
| p41 p77
p63: p91 p123
| p77 p10
p82: p89 p91
| p80 p77
p6: p91 p50
| p77 p14
p129: p84 p28
p55: p56 p91
| p94 p77
p70: p77 p93
| p91 p88
p58: p22 p77
| p22 p91
p81: p22 p77
| p68 p91
p3: p77 p16
| p91 p78
p40: p34 p91
| p84 p77
p36: p121 p91
| p30 p77
p127: p91 p21
| p77 p48
p115: p91 p91
| p91 p77
p96: p77 p97
p71: p77 p84
| p91 p105
p83: p22 p77
| p100 p91
p118: p84 p77
p84: p28 p77
| p77 p91
p43: p77 p84
| p91 p22
p69: p77 p60
| p91 p108
p68: p91 p77
| p77 p77
p97: p77 p77
p100: p77 p91
p28: p77
| p91
p113: p91 p77
| p77 p91
p33: p77 p61
| p91 p103
p5: p91 p1
| p77 p87
p78: p34 p91
| p97 p77
p74: p58 p91
| p129 p77
p16: p14 p77
| p84 p91
p26: p95 p77
| p32 p91
p34: p28 p28
p92: p55 p77
| p66 p91
p116: p77 p102
| p91 p70
p7: p98 p91
| p2 p77
p59: p61 p91
| p17 p77
p121: p64 p91
| p18 p77
p60: p91 p29
| p77 p62
p12: p77 p13
| p91 p122
p49: p124 p28
p124: p77 p91
| p77 p77
p114: p77 p115
| p91 p24
p80: p86 p77
| p81 p91
p128: p67 p77
| p9 p91
p86: p14 p77
| p105 p91
p119: p77 p85
| p91 p4
p14: p91 p91
| p77 p77
p19: p91 p68
| p77 p34
p15: p84 p77
| p115 p91
p117: p73 p77
| p57 p91
p103: p91 p105
| p77 p24
p13: p91 p14
| p77 p50
p17: p22 p91
| p115 p77

                 %import common.WS
                 %ignore WS
         ''', start='p0')

total = 0

with open('19.txt') as f:
    for line in f:
        if m := re.match('(\d+): (.*)', line):
            pass

        elif line == "\n":
            pass

        else:
            try:
                parser.parse(line)
                total += 1
                print(line)
            except:
                pass

print(total)
