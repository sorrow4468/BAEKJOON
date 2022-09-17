import sys
from collections import deque

input = sys.stdin.readline

def BFS(node):
    global result
    Q.append(node)
    visited[node] = 1
    cnt = 0
    while Q:
        now = Q.popleft()
        for next in arr[now]:
            if not visited[next]:
                Q.append(next)
                visited[next] = 1
                cnt += 1
    result -= cnt

N, M = map(int, input().rstrip().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
Q = deque()
for m in range(M):
    u, v = map(int, input().rstrip().split())
    arr[u].append(v)
    arr[v].append(u)
result = N
for i in range(1, N+1): 
    BFS(i)
    if sum(visited) == N: break
print(result)