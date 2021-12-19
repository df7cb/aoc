#!/usr/bin/python3

import binarytree
from binarytree import Node, get_parent

numbers = []

def maketree(a):
    if type(a) is int:
        return Node(a)
    else:
        x = Node(-1)
        x.left = maketree(a[0])
        x.right = maketree(a[1])
        return x

def makelist(a):
    if a.left is None:
        return a.value
    else:
        return [makelist(a.left), makelist(a.right)]

with open('18.txt') as f:
    for line in f:
        a = eval(line)
        numbers.append(a)

def leaf_depth(root, node):
    if root == node:
        return 0
    return 1 + leaf_depth(root, get_parent(root, node))

def left_neighbor(root, node):
    found = False
    nodes = [x for x in root.inorder]
    nodes.reverse()
    for n in nodes:
        if n == node:
            found = True
        elif found and n.value >= 0:
            return n
    return None

def right_neighbor(root, node):
    found = False
    for n in root.inorder:
        if n == node:
            found = True
        elif found and n.value >= 0:
            return n
    return None

def explode(root):
    for node in root.inorder:
        if node.value >= 0 and leaf_depth(root, node) > 4:
            parent = get_parent(root, node)
            parent.value = 0
            ln = left_neighbor(root, parent.left)
            if ln:
                ln.value += parent.left.value
            rn = right_neighbor(root, parent.right)
            if rn:
                rn.value += parent.right.value
            parent.left = None
            parent.right = None
            return True
    return False

def split(root):
    for node in root.inorder:
        if node.value >= 10:
            node.left = Node(node.value // 2)
            node.right = Node(node.value - node.value // 2)
            node.value = -1
            return True
    return False

def reduce(root):
    while True:
        if root.max_leaf_depth > 4:
            explode(root)
            #print("explode:", root)
        elif split(root):
            #print("split:", root)
            pass
        else:
            break

    return root

def magnitude(a):
    if a.left is None:
        return a.value
    else:
        return 3 * magnitude(a.left) + 2 * magnitude(a.right)

best = None

for n1 in range(len(numbers)):
    for n2 in range(len(numbers)):
        print(n1, n2)
        if n1 == n2:
            continue

        s = Node(-1)
        s.left = maketree(numbers[n1])
        s.right = maketree(numbers[n2])
        reduce(s)
        print(s)
        mag = magnitude(s)
        if best is None or mag > best:
            best = mag
        print(best, mag, makelist(s))
