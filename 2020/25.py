#!/usr/bin/python3

#door = 17807724
#card = 5764801
door = 16915772
card = 18447943

door_loop = None
card_loop = None

value = 1

round = 1
while True:
    if round % 1000000 == 0:
        print(round)
    value = (value * 7) % 20201227
    if value == door and door_loop is None:
        door_loop = round
        if card_loop:
            break
    if value == card and card_loop is None:
        card_loop = round
        if door_loop:
            break
    round += 1

print('door:', door_loop, door)
print('card:', card_loop, card)

value = 1
for i in range(door_loop):
    value = (value * card) % 20201227
print('encryption key:', value)

value = 1
for i in range(card_loop):
    value = (value * door) % 20201227
print('encryption key:', value)
