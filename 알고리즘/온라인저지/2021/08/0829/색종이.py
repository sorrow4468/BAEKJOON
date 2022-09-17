import sys

N = int(sys.stdin.readline())
board = [[0]*1002 for _ in range(1002)]
max_y = 0
max_x = 0
for n in range(1, N+1):
    Y, X, H, W = map(int, sys.stdin.readline().split())
    for y in range(Y, Y+H):
        for x in range(X, X+W):
            board[y][x] = n
            if max_y < y:
                max_y = y
            if max_x < x:
                max_x = x
result = [0] * N
for n in range(1, N+1):
    for i in range(max_y+1):
        for j in range(max_x+1):
            if board[i][j] == n:
                result[n-1] += 1
for r in result:
    print(r)