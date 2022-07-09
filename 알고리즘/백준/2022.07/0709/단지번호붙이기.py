from collections import deque


def bfs(y, x):
    Q.append((y, x))
    cnt = 0
    while Q:
        y, x = Q.popleft()
        if arr[y][x] == 0:
            continue
        arr[y][x] = 0
        cnt += 1
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<N and arr[ny][nx]:
                Q.append((ny, nx))
    return cnt


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
result = [0]
Q = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            result.append(bfs(i, j))
            result[0] += 1
print(result[0])
for r in sorted(result[1:]): print(r)