#!/usr/bin/python3

#traps = '..^^.'
#traps = '.^^.^.^^^^'
traps = '.^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^'

def next(traps):
    traps_with_wall = '.' + traps + '.'
    next_traps = ''
    for p in range(1, len(traps_with_wall)-1 ):
        neigh = traps_with_wall[p-1:p+2]
        if neigh in ['..^', '^..', '.^^', '^^.']:
            next_traps += '^'
        else:
            next_traps += '.'

    return next_traps

safe = 0
#for i in range(40):
for i in range(400000):
    print(i, traps)
    safe += len([x for x in traps if x == '.'])
    traps = next(traps)

print('18a/b:', safe)
