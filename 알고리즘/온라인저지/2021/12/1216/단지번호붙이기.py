from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

N = int(input())

map = [list(map(int, input())) for _ in range(N)]

complex_cnt = 0

complex_counts = []

bfs = deque()

for i in range(N):
    for j in range(N):
        if map[i][j]:
            bfs.append((i, j))
            complex_cnt += 1
            cnt = 0
            while bfs:
                tmp = bfs.popleft()
                y = tmp[0]
                x = tmp[1]

                if map[y][x] == 0:
                    continue
                
                map[y][x] = 0
                cnt += 1

                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]

                    if 0 <= ny < N and 0 <= nx < N and map[ny][nx]:
                        bfs.append((ny, nx))
            complex_counts.append(cnt)
print(complex_cnt)
complex_counts.sort()
for c in complex_counts:
    print(c)