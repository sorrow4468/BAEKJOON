H, W, N, M = map(int, input().split())
result = 0
for i in range(0, H, 1+N):
    for j in range(0, W, 1+M):
        result += 1
print(result)