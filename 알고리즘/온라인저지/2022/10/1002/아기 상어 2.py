import sys
from collections import deque

input = sys.stdin.readline
dy = [-1, -1, 0, 1, 1, 1, 0, -1] # 12시부터 시계방향
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def BFS(i, j):
    visited = [[0]*M for _ in [0]*N]
    Q = deque()
    Q.append((i, j, 0))
    visited[i][j] = 1
    while Q:
        y, x, dist = Q.popleft()
        if arr[y][x]: break
        for k in range(8):
            ny, nx = y+dy[k], x+dx[k]
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
                Q.append((ny, nx, dist+1))
                visited[ny][nx] = 1
    return dist

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in [0]*N]
result = 0
for i in range(N):
    for j in range(M):
        result = max(result,BFS(i, j))
print(result)

"""
매 좌표마다 상어안전거리를 구한다 : brute force
새 최소값을 매 회마다 갱신한다
"""