import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split()) # 정점수, 간선수
# 인접 행렬
G = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = 1

for lst in G[1:]:
    print(*lst[1:])

# 인접 리스트
G = [[]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, V+1):
    print(i, '-->', G[i])
