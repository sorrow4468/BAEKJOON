import sys

def dfs(v):
    visited[v] = 1
    global cnt
    cnt += 1
    for w in range(1, V+1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

G = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    G[u][v] = G[v][u] = 1

visited = [0] * (V+1)
cnt = -1
dfs(1)
print(cnt)