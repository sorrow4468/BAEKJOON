from collections import deque
import sys


def input():
    return sys.stdin.readline()

def bfs(i, j):
    q.append((i, j))
    now = arr[i][j]
    while q:
        y, x = q.popleft()
        visited[y][x] = 1
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and arr[ny][nx] == now:
                if (ny, nx) not in q:
                    q.append((ny, nx))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N = int(input())
arr = [list(input()) for _ in range(N)]
NCB = 0 # Non Color Blindness
CB = 0 # Color Blindness
visited = [[0]*N for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            NCB += 1
        if arr[i][j] in 'RG':
            arr[i][j] = 'Y'
visited = [[0]*N for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            CB += 1
print(NCB, CB)