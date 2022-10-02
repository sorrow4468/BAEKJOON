import sys
from collections import deque

input = sys.stdin.readline
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in [0]*int(input().rstrip()):
    L = int(input().rstrip())
    start = tuple(map(int, input().rstrip().split()))
    goal = tuple(map(int, input().rstrip().split()))
    result = 0
    visited = [[0]*L for l in [0]*L]
    Q = deque()
    y, x = start
    Q.append((y, x, 0))
    visited[y][x] = 1
    while Q:
        y, x, move = Q.popleft()
        if (y, x) == goal: result = move; break
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<L and 0<=nx<L and not visited[ny][nx]:
                Q.append((ny, nx, move+1))
                visited[ny][nx] = 1
    print(move)