"""
0: 4
1: 4+5 = 9
2: 9+ 

4
4*4-4-3
9*4-8-3


dp[i] = dp[i-1] * 4 - (4*i+3)
"""

N = int(input())

dp = [4]

tmp = 4

for i in range(1, N+1):
    dp.append(dp[i-1] * 4 - (tmp+3))
    tmp *= 2

print(dp[N])