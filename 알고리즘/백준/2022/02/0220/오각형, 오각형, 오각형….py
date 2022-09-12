"""
0 : 1
1 : 1 1 1 1 1
2 : 5 1 2 2 2 
3 : 12 1 3 3 3
4 : 22 1 4 4 4
5 : 35 1 5 5 5
"""

N = int(input())

dp = [1]

for i in range(1, N+1):
    dp.append(dp[i-1] + 1 + i*3)

print(dp[-1]%45678)