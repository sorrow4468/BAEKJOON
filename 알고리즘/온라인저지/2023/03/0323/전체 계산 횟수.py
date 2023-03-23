N, M = map(int, input().split())
result = N
while N:
    N //= M
    result += N
print(result)