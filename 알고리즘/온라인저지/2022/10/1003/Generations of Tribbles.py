import sys

input = sys.stdin.readline

dp = [1, 1, 2, 4] + [0]*66
for i in range(4, 70):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4]
for i in [0]*int(input().rstrip()):
    print(dp[int(input().rstrip())])