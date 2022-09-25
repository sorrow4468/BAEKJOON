import sys

input = sys.stdin.readline

N = int(input().rstrip())
dp = [0, 1, 0, 1, 1] + [0]*(N-4)
if N>4:
    for i in range(5, N+1):
        if 0 in [dp[i-1], dp[i-3], dp[i-4]]:
            dp[i] = 1
        else: dp[i] = 0
print('SK' if dp[N] else 'CY')

# https://www.acmicpc.net/problem/9657