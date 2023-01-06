S = input()
P = input()
i = 0
for s in S:
    if s != ' ':
        tmp = ord(s) - (ord(P[i])-96)
        if not tmp >= 97: tmp += 26
        print(chr(tmp), end='')
    else: print(' ', end='')
    i = (i+1)%len(P)