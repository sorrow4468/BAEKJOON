import sys

input = sys.stdin.readline

N, m, M, T, R = map(int, input().rstrip().split())
n = 0
result = 0
now = m
while n < N:
    result += 1
    # print(result, now, T, R)
    if m+T > M:
        result = -1
        break
    if now+T <= M:
        n += 1
        now += T
    else:
        if now-R <= m:
            now = m
        else:
            now -= R
print(result)