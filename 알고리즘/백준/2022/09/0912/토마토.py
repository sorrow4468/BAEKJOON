from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Q.append((i, j, 0))
            arr[i][j] = 0
result = 0
while Q:
    y, x, day = Q.popleft()
    if arr[y][x] == 1: continue
    arr[y][x] = 1
    result = max(result, day)
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 0:
            Q.append((ny, nx, day+1))
for i in range(N):
    if result == -1: break
    for j in range(M):
        if arr[i][j] == 0:
            result = -1
            break
print(result)

# https://www.acmicpc.net/problem/7576