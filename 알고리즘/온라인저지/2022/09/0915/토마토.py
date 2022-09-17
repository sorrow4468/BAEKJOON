from collections import deque

# 상 하 전 후 좌 우 델타이동
dz, dy, dx = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
Q = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                Q.append((k, i, j, 0)) # z, y, x, day
                arr[k][i][j] = 0
result = 0
while Q:
    z, y, x, day = Q.popleft()
    if arr[z][y][x] == 1: continue
    arr[z][y][x] = 1
    result = max(result, day)
    for i in range(6): # 상 하 전 후 좌 우
        nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
        if 0<=nz<H and 0<=ny<N and 0<=nx<M and arr[nz][ny][nx] == 0:
            Q.append((nz, ny, nx, day+1))
for k in range(H):
    if result == -1: break
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 0:
                result = -1
                break
print(result)

# https://www.acmicpc.net/problem/7569