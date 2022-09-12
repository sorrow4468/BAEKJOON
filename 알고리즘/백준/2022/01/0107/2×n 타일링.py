N = int(input())

dp = [0 for _ in range(N+1)]

dp[1] = 1
if N == 1:
    print(dp[N])
    
else:
    dp[2] = 2

    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

    print(dp[N])

"""
1 1
2 2
3 3
4 5
5 8
6 13
7 21
8 34
9 55
"""