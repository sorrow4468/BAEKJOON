import sys
C, R = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

hall = [[0]*C for _ in range(R)]
i = 1
x = y = k = 0

while i < K:
    hall[y][x] = i
    i += 1
    if x+dx[k] >= C or y+dy[k] >= R or hall[y+dy[k]][x+dx[k]]:
        k = (k+1)%4
    x = (x+dx[k])
    y = (y+dy[k])
if C*R < K:
    print(0)
else:
    print(x+1, y+1)