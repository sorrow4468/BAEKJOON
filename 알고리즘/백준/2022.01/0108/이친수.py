"""
1 1
1

2 1
10

3 2
100
101

4 3
1000
1001
1010

5 5
10000
10001
10010
10100
10101
"""

N = int(input())

dp = [0 for _ in range(91)]

dp[1], dp[2] = 1, 1

if N < 3:
    print(dp[N])
    exit()

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])