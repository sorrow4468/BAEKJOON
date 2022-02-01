T = int(input())

dp = [0] * 42
dp[1] = 1

for i in range(2, 42):
    dp[i] = dp[i-1] + dp[i-2]

for t in range(T):
    N = int(input())

    if N == 0:
        print(1, 0)
    else:
        print(dp[N-1], dp[N])