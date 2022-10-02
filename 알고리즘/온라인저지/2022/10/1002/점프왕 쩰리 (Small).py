import sys
from collections import deque

input = sys.stdin.readline
dy, dx = [1, 0], [0, 1] # down, right

N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
Q = deque()
Q.append((0, 0))
visited[0][0] = 1
while Q:
    y, x = Q.popleft()
    if y == x == N-1: print('HaruHaru'); break
    jump = arr[y][x]
    for i in range(2):
        ny, nx = y+dy[i]*jump, x+dx[i]*jump
        if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
            Q.append((ny, nx))
            visited[ny][nx] = 1
else: print('Hing')