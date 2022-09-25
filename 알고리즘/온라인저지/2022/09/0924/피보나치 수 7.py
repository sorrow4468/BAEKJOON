import sys

input = sys.stdin.readline

N = int(input().rstrip())
dp = [0, 1] + [0]*int(1e7)
for i in range(2, int(1e7)):
    dp[i] = (dp[i-1] + dp[i-2])%1000000007
print(dp[N])