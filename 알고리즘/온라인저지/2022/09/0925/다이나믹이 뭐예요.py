import sys

input = sys.stdin.readline
dy, dx = [0, 1, 1], [1, 0, 1] # right, down, right-down
mod = int(1e9)+7

N, M = map(int, input().rstrip().split())
dp = [[0]*M for _ in range(N)]
y, x = 0, 0
for i in range(N): dp[i][0] = 1
for i in range(M): dp[0][i] = 1
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1])%mod
print(dp[N-1][M-1])

# https://www.acmicpc.net/problem/14494