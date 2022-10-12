import sys

input = sys.stdin.readline
INF = int(1e9)

N, K = map(int, input().rstrip().split())
coins = set()
for i in range(N):
    coins.add(int(input().rstrip()))
coins = list(coins)
dp = [INF]*(K+1)
dp[0] = 0
for i in range(K+1):
    for coin in coins:
        if i+coin <= K:
            dp[i+coin] = min(dp[i]+1, dp[i+coin])
print(dp[K] if dp[K] != INF else -1)