import sys

input = sys.stdin.readline

N = int(input().rstrip())
dp = [0]*36
dp[0] = 1
for i in range(35):
    tmp = 0    
    for j in range(i+1):
        tmp += dp[j]*dp[i-j]
    dp[i+1] = tmp
print(dp[N])

# https://www.acmicpc.net/problem/13699