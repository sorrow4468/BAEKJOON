dx = [1, 0]
dy = [0, 1]

def dfs(x, y, tmp):
    global result
    if x == N-1 and y == N-1:
        if tmp < result:
            result = tmp

    if tmp > result:
        return

    for i in range(2):
        visited[y][x] = 1
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and visited[ny][nx] == 0:
            dfs(nx, ny, tmp+arr[ny][nx])
        visited[y][x] = 0

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(list(map(int, input().split())))
    
    visited = [[0]*N for _ in range(N)]

    result = 99999999
    dfs(0, 0, arr[0][0])
    print('#{} {}'.format(tc, result))