"""
0
1
10
101
10110

1 1
1 2
2 3
3 4
5 5
8 6
13 7
21 8
34 9

"""

dp = [0, 1, 1]

K = int(input())


if K <= 2:
    print(dp[K-1], dp[K])
else:
    for i in range(3, K+1):
        dp.append(dp[i-1] + dp[i-2])

    print(dp[K-1], dp[K])

