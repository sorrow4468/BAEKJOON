from collections import deque


def bfs(y, x):
    Q.append((y, x))
    global maxx
    tmp = 0
    while Q:
        y, x = Q.popleft()
        if arr[y][x] == 0:
            continue
        arr[y][x] = 0
        tmp += 1
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M and arr[ny][nx]:
                Q.append((ny, nx))
    if tmp > maxx:
        maxx = tmp


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = maxx = 0
Q = deque()
for n in range(N):
    for m in range(M):
        if arr[n][m]:
            bfs(n, m)
            result += 1
print(result)
print(maxx)