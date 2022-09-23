import sys

input = sys.stdin.readline
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0] # 우 하 좌 상

def check_goal(y, x):
    flag = True
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<N and 0<=nx<M and not arr[ny][nx]: 
            flag = False
    return flag

N, M = map(int, input().rstrip().split())
result = 0
arr = [[0]*M for _ in range(N)]
y, x = 0, 0
i = 0
while True:
    if check_goal(y, x): break
    arr[y][x] = 1
    ny, nx = y+dy[i], x+dx[i]
    if not (0<=ny<N and 0<=nx<M) or arr[ny][nx]:
        i = (i+1)%4
        ny, nx = y+dy[i], x+dx[i]
        result += 1
    y, x = ny, nx
print(result)