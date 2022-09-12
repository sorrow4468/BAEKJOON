N = int(input())

if N == 0:
    print(0)
else:
    dp = [0] * (N+1)
    dp[1] = 1

    if N == 1:
        print(1)
    else:
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp[-1])