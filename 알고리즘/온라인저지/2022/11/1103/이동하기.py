import sys

input = sys.stdin.readline
dy, dx = [1, 0, 1], [0, 1, 1]

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [a[:] for a in arr]
for i in range(N):
    for j in range(M):
        for k in range(3):
            ny, nx = i+dy[k], j+dx[k]
            if 0<=ny<N and 0<=nx<M:
                dp[ny][nx] = max(dp[ny][nx], arr[ny][nx]+dp[i][j])
print(dp[N-1][M-1])