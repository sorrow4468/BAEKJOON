import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
Q = deque()
visited = [0]*N
Q.append((0, 0))
visited[0] = 1
while Q:
    now, move = Q.popleft()
    if now == N-1: print(move); break
    for i in range(now+1, now+1+arr[now]):
        if 0<=i<N and arr[i] and not visited[i]:
            Q.append((i, move+1))
            visited[i] = 1
else: print(-1)