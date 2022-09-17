import copy
from collections import deque

N = int(input())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

height_map = [list(map(int, input().split())) for _ in range(N)]

rain = 0

bfs = deque()

result = 0

while True:
    tmp_map = copy.deepcopy(height_map)

    flooded_check = 0
    for i in range(N):
        for j in range(N):
            if tmp_map[i][j] <= rain:
                tmp_map[i][j] = 0
        flooded_check += sum(tmp_map[i])
    
    if flooded_check == 0:
        break
    
    safe = 0 # 현재 rain에서 나온 안전영역의 수

    for i in range(N):
        for j in range(N):
            if tmp_map[i][j]:
                bfs.append((i, j))
                safe += 1

                while bfs:
                    tmp = bfs.popleft()
                    y = tmp[0]
                    x = tmp[1]

                    if tmp_map[y][x] == 0:
                        continue
                    
                    tmp_map[y][x] = 0
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if 0 <= ny < N and 0 <= nx < N and tmp_map[ny][nx]:
                            bfs.append((ny, nx))

    rain += 1
    
    if safe > result:
        result = safe

print(result)