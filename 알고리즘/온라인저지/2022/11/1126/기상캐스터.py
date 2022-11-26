import sys

input = sys.stdin.readline
INF = int(1e9)
H, W = map(int, input().rstrip().split())
result = [[INF]*W for _ in range(H)]
arr = [input().rstrip() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            for k in range(W):
                if j+k < W:
                    result[i][j+k] = min(result[i][j+k], k)
for i in range(H):
    for j in range(W):
        if result[i][j] == INF:
            result[i][j] = -1
for r in result: print(*r)