import sys

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(y, x, move, str_num):
    if move == 5: 
        result.add(int(str_num))
        return
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0<=ny<5 and 0<=nx<5:
            dfs(ny, nx, move+1, str_num+str(arr[ny][nx]))

arr = [list(map(int, input().rstrip().split())) for _ in range(5)]
result = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, 0, str(arr[i][j]))
print(len(result))