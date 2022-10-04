import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input().rstrip())
dp = [INF]*(int(1e5)+10)
dp[0], dp[1], dp[2], dp[5], dp[7] = 0, 1, 1, 1, 1
for i in range(1, int(1e5)+1):
    tmp = dp[i]+1
    if dp[i]:
        dp[i+1] = min(dp[i+1], tmp)
        dp[i+2] = min(dp[i+2], tmp) 
        dp[i+5] = min(dp[i+5], tmp) 
        dp[i+7] = min(dp[i+7], tmp)
print(dp[N])