from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]

    for k in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    worm = deque()
    cnt = 0

    for i in range(N):
        for j in range(M):
            if field[i][j]:
                worm.append((i, j))
                cnt += 1
                while worm:
                    tmp = worm.popleft()
                    y = tmp[0]
                    x = tmp[1]
                    if field[y][x]:
                        field[y][x] = 0
                    else:
                        continue
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < M and 0 <= ny < N and field[ny][nx]:
                            worm.append((ny, nx))

    print(cnt)