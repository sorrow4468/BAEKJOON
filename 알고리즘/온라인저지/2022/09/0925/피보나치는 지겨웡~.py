import sys

input = sys.stdin.readline

N = int(input().rstrip())
mod = int(1e9)+7
dp = [0] * (N+30)
dp[0], dp[1] = 1, 1
if N>1:
    for i in range(2, N+1):
        dp[i] = (dp[i-1] + dp[i-2] + 1)%mod
print(dp[N])