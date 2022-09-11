N = int(input())
wines = [0] * 10002
dp = [0] * 10002
for n in range(N): wines[n] = int(input())
dp[0] = wines[0]
dp[1] = max(dp[0], wines[0]+wines[1])
dp[2] = max(dp[1], wines[1]+wines[2], wines[0]+wines[2])
for i in range(3, N):
    A = dp[i-3] + wines[i-1] + wines[i]
    B = dp[i-2] + wines[i]
    dp[i] = max(A, B, dp[i-1])
print(max(dp))