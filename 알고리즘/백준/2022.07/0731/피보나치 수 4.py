N = int(input())
dp = [0, 1]
if N > 1: dp += [0] * (N-1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[-1]) if N != 0 else print(0)