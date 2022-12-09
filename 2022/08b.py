#!/usr/bin/python3

with open("08.txt") as f:
    forest = [x.strip() for x in f]

best_score = 0
for y in range(len(forest)):
    for x in range(len(forest[0])):
        tree = forest[y][x]

        xx = x - 1
        ltrees = 0
        while xx >= 0:
            ltrees += 1
            if forest[y][xx] >= tree:
                break
            xx -= 1

        xx = x + 1
        rtrees = 0
        while xx < len(forest[0]):
            rtrees += 1
            if forest[y][xx] >= tree:
                break
            xx += 1

        yy = y - 1
        utrees = 0
        while yy >= 0:
            utrees += 1
            if forest[yy][x] >= tree:
                break
            yy -= 1

        yy = y + 1
        dtrees = 0
        while yy < len(forest):
            dtrees += 1
            if forest[yy][x] >= tree:
                break
            yy += 1

        score = ltrees * rtrees * utrees * dtrees
        print(y, x, '', ltrees, rtrees, utrees, dtrees, '', score)

        best_score = max(best_score, score)

print(best_score)

