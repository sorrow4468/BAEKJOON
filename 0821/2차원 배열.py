N = 100
arr = [[0]*N for _ in range(N)]

#1
for i in range(N):
    for j in range(N):
        arr[j][i] = 1

#2
for j in range(N):
    for i in range(N):
        arr[i][j] = 1

#3
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
k = 0
for i in range(N):
    for j in range(N):
        now = arr[i][j]
        go_to = arr[i+dy[k]][j+dx[k]]

#4
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

#5
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def add_abs(x, y, n):
    total = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            total += abs(arr[x][y] - arr[nx][ny])

    return total

tc = int(input())

for idx in range(1, tc+1):
    n = int(input())
    total = 0
    for x in range(n):
        for y in range(n):
            total += add_abs(x, y, n)

