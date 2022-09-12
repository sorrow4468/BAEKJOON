INF = int(1e9)
N, K = map(int, input().split())
world = [[INF]*N for _ in range(N)]
for k in range(K):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    world[A][B], world[B][A] = 1, 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j:
                world[i][j] = min(world[i][j], world[i][k]+world[k][j])
result = 'Small World!'
for i in range(N):
    if result != 'Small World!':
        break
    for j in range(N):
        if i != j:
            if world[i][j] > 6:
                result = 'Big World!'
                break
print(result)

# https://www.acmicpc.net/problem/18243