#!/usr/bin/python3

#Player 1 starting position: 6
#Player 2 starting position: 7

pos = [6, 7]
#pos = [4, 8]
score = [0, 0]

roll = 1
rolls = 0
def die():
    global roll
    global rolls
    ret = roll
    roll += 1
    rolls += 1
    if roll > 100:
        roll = 1
    return ret

def move(player):
    pos[player] = (pos[player] + die() + die() + die()) % 10
    score[player] += pos[player] if pos[player] > 0 else 10
    print(player, pos, score)

turn = 0
while True:
    move(turn)
    if score[turn] >= 1000:
        print("Player", turn, "wins after", rolls, "die rolls")
        print(pos, score)
        break
    turn = 1 - turn

print("Result", score[1 - turn] * rolls)
