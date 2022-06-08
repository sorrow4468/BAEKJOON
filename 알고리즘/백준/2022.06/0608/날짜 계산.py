E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
result = 1
while (E, S, M) != (e, s, m):
    e, s, m, result = e+1, s+1, m+1, result+1
    if e > 15:
        e -= 15
    if s > 28:
        s -= 28
    if m > 19:
        m -= 19
print(result)