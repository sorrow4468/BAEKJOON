N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
for k in range(N):
    for a in range(N):
        for b in range(N):
            if arr[a][k] and arr[k][b]:
                arr[a][b] = 1
for s in range(int(input())):
    a, b = map(int, input().split())   
    result = 0
    if arr[a-1][b-1]:
        result = -1
    elif arr[b-1][a-1]:
        result = 1
    print(result)

# https://www.acmicpc.net/problem/1613