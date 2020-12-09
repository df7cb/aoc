#!/usr/bin/python3

password = list('hxbxwxba')
print("".join(password))

def inc(t):
    for p in range(len(t)-1, -1, -1):
        if t[p] == 'z':
            t[p] = 'a'
            continue
        t[p] = chr(ord(t[p])+1)
        if t[p] == 'i' or t[p] == 'o' or t[p] == 'l':
            t[p] = chr(ord(t[p])+1)
        break
    return t

def check(t):
    for p in range(len(t)-2):
        if ord(t[p]) == ord(t[p+1]) - 1 == ord(t[p+2]) - 2:
            break
    else:
        return False
    for p in range(len(t)-1):
        if t[p] == t[p+1]:
            for p2 in range(p+2, len(t)-1):
                if t[p]!=t[p2] and t[p2] == t[p2+1]:
                    return True
    return False

while not check(password):
    #print(password)
    inc(password)

print("".join(password))

inc(password)
while not check(password):
    #print(password)
    inc(password)

print("".join(password))
