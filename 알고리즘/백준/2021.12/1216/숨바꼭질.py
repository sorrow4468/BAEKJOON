from collections import deque

N, K = map(int, input().split())

bfs = deque()
bfs.append((N, 0))

visited = [0 for _ in range(100001)]

while bfs:
    tmp = bfs.popleft()
    n = tmp[0]
    t = tmp[1]

    if visited[n]:
        continue

    if n == K:
        print(t)
        break

    visited[n] = 1

    go = n+1
    back = n-1
    jump = n*2

    if 0 <= go <= 100000 and not visited[go]:
        bfs.append((go, t+1))
    if 0 <= back <= 100000 and not visited[back]:
        bfs.append((back, t+1))
    if 0 <= jump <= 100000 and not visited[jump]:
        bfs.append((jump, t+1))