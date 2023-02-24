L, R, A = map(int, input().split())

while A:
    if L > R:
        R += 1
        A -= 1
    elif L < R:
        L += 1
        A -= 1
    else:
        if A == 1:
            break
        else:
            L += 1
            A -= 1

print(min(L, R)*2)