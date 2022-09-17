INF = int(1e9)
N = int(input())
M = int(input())
arr = [[INF]*N for _ in range(N)]
for m in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    if c < arr[a][b]:
        arr[a][b] = c
for k in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
for i in range(N):
    for j in range(N):
        if i == j:
            arr[i][j] = 0 
        if arr[i][j] == INF:
            arr[i][j] = 0
for a in arr: print(*a)