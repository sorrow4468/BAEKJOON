N, _ = map(int, input().split())
M = list(map(int, input().split()))
N = list(range(1, N+1))
prev = 0
result = 0
for m in M:
    i = N.index(m)
    D = abs(prev - i)
    D = min(D, len(N)-D)
    result += D
    N.pop(i)
    prev = i
print(result)