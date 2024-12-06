#!/usr/bin/python3

rules = []
updates = []

with open("05.txt") as f:
    for line in f:
        if line.strip() == "":
            break
        rules.append([int(x) for x in line.split(r'|')])
    for line in f:
        updates.append([int(x) for x in line.split(r',')])

#print(rules)
#print(updates)

def check(u):
    #print(u)
    for r in rules:
        if r[0] not in u or r[1] not in u: continue
        a = u.index(r[0])
        b = u.index(r[1])
        if a > b:
            #print(r, a, b)
            return False
    return True

res = 0

for u in updates:
    if check(u):
        middle = u[len(u) // 2]
        #print(u, middle)
        res += middle

print(res)
