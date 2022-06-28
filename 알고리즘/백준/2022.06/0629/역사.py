INF = int(0)
N, M = map(int, input().split())
arr = [[INF]*N for _ in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    arr[a][b] = 1
for k in range(N):
    for a in range(N):
        for b in range(N):
            if arr[a][k] and arr[k][b]:
                arr[a][b] = 1
S = int(input())
for s in range(S):
    a, b = map(int, input().split())    
    a, b = a-1, b-1
    result = 0
    if arr[a][b]:
        result = -1
    elif arr[b][a]:
        result = 1
    print(result)