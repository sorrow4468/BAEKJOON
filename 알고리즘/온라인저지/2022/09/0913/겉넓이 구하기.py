dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
zero = 0
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0: 
            zero += 1
            continue
        now = arr[i][j]
        while now > 0:
            face = 4 # 도형의 면
            if now == arr[i][j]: face += 1
            y, x = i, j
            for k in range(4):
                ny, nx = y+dy[k], x+dx[k]
                if 0<=ny<N and 0<=nx<M:
                    if arr[ny][nx] >= now:
                        face -= 1
            result += face
            now -= 1    
print(result + N*M - zero)

# https://www.acmicpc.net/problem/16931