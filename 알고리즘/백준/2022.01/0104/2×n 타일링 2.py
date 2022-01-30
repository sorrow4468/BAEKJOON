N = int(input())

dp = [0 for _ in range(N+1)]

dp[1] = 1
if N >= 2:
    dp[2] = 3
    if N == 2:
        print(dp[2])
        exit()
if N >= 3:
    dp[3] = 5
    if N == 3:
        print(dp[3])
        exit()

for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[N]%10007)

# 0
# 1
# 3
# 5
# 11
# 21
# 43
# 85
# 171

