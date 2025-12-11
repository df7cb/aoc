#!/usr/bin/python3

connections = {}

with open("11.txt") as f:
    for line in f:
        l, r = line.split(": ")
        connections[l] = r.split()

def walk(node, target, nums):
    if node in nums:
        return nums[node]

    if node == target:
        return 1
    if node == "out":
        return 0

    num = 0
    for n in connections[node]:
        num += walk(n, target, nums)
    nums[node] = num
    return num

num = walk("svr", "fft", {}) * walk("fft", "dac", {}) * walk("dac", "out", {}) \
    + walk("svr", "dac", {}) * walk("dac", "fft", {}) * walk("fft", "out", {})

print(num)
