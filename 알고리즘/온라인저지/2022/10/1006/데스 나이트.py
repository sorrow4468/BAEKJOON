import sys
from collections import deque

input = sys.stdin.readline
dy = [-2, -2, 0, 0, 2, 2]
dx = [-1, 1, -2, 2, -1, 1]

N = int(input().rstrip())
r1, c1, r2, c2 = map(int, input().rstrip().split())
visited = [[0]*N for _ in range(N)]
Q = deque()
Q.append((r1, c1, 0))
visited[r1][c1] = 1
result = -1
while Q:
    y, x, move = Q.popleft()
    if y == r2 and x == c2: result = move; break
    for i in range(6):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
            Q.append((ny, nx, move+1))
            visited[ny][nx] = 1
print(result)