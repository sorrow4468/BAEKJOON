import sys

input = sys.stdin.readline

N = int(input().rstrip())
dp = list(map(int, input().rstrip().split()))
min_num = dp[0]
dp[0] = 0
for i in range(1, N):
    min_num = min(min_num, dp[i])
    dp[i] = max(dp[i]-min_num, dp[i-1])
print(*dp)