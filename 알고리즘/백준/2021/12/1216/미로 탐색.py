from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

routes = deque()

routes.append((0, 0, 0))

while routes:
    tmp = routes.popleft()
    y = tmp[0]
    x = tmp[1]
    cnt = tmp[2]
    
    if y == N-1 and x == M-1:
        print(cnt + 1)
        break

    if maze[y][x] == 0:
        continue

    maze[y][x] = 0

    cnt += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M and maze[ny][nx]:
            routes.append((ny, nx, cnt))

