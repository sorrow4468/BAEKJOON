import sys

input = sys.stdin.readline

N = int(input())
dp = [0, 1, 1, 1] + [0]*114
for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-3]
print(dp[N])