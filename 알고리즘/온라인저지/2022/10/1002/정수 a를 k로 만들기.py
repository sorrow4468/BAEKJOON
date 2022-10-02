import sys
from collections import deque

input = sys.stdin.readline

def move(next, new_cnt):
    if 0<=next<mxl and not visited[next]:
        Q.append((next, new_cnt))
        visited[next] = 1

A, K = map(int, input().rstrip().split())
mxl = int(1e6)+1 # max_length
visited = [0]*mxl
Q = deque()
Q.append((A, 0))
visited[A] = 1
result = 0
while Q:
    now, cnt = Q.popleft()
    if now == K: result = cnt; break
    move(now+1, cnt+1)
    move(now*2, cnt+1)
print(result)