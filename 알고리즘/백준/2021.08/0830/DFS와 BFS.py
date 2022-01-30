import sys

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, N+1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)

def bfs(v, n):
    q = []
    visited = [0] * (N+1)
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(t, end=' ')
        for i in range(1, N+1):
            if G[t][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1

N, M, V = map(int, sys.stdin.readline().split())

G = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    G[u][v] = G[v][u] = 1

visited = [0] * (N+1)
dfs(V)
print()

visited = [0] * (N+1)
bfs(V, N)