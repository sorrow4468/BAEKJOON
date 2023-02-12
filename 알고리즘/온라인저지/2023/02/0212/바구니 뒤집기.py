N, M = map(int, input().split())
result = list(range(1, N+1))
for m in range(M):
    i, j = map(int, input().split())
    i -= 1
    result = result[:i] + result[i:j][::-1] + result[j:]
print(*result)