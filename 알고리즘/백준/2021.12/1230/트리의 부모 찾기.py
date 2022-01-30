import sys
sys.setrecursionlimit(99999)

def dfs(i):
    for n in nodes[i]:
        if not parent[n]:
            parent[n] = i
            dfs(n)

N = int(input())

nodes = [[] for _ in range(N+1)]

parent = [0 for _ in range(N+1)]
parent[1] = 'root'

for n in range(N-1):
    a, b = map(int, input().split())
    
    nodes[a].append(b)
    nodes[b].append(a)

dfs(1)

for p in parent[2:]:
    print(p)