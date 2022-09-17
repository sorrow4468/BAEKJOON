"""
[0, 1, 2, 3, 5]

1
1

2
00
11

3
100
001
111

4
0000      
0011
1001
1100
1111
"""

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    dp = [0 for _ in range(N+1)]
    dp[1], dp[2] = 1, 2

    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    
    print(dp[N])