#!/usr/bin/python3

freq = 0
seen = {}
seen[freq] = 1

while True:
    with open("01.txt") as f:
        for line in f:
            freq += int(line)
            if freq in seen:
                print("We have seen", freq, "before")
                exit()
            seen[freq] = 1
