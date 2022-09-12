def rev(num):
    return int(str(num)[::-1])

X, Y = map(int, input().split())

print(rev(rev(X)+rev(Y)))