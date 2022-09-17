N = int(input())

if N > 1:
    dp = [0] * (N+1)
    dp[1] = 1

    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[-1])

else:
    if N:
        print(1)
    else:
        print(0)