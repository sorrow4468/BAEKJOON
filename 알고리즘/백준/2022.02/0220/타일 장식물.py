"""
1 : 1+1+1+1
2 : 4-1+1+1+1
3 : 6-2+2+2+2
4 : 10-3+3+3+3
5 : 
1 : 
"""

N = int(input())

result = [0, 4]

dp = [0, 1]

if N >= 2:
    for i in range(2, N+1):
        dp.append(dp[i-1] + dp[i-2])

    for i in range(2, N+1):
        result.append(result[i-1] + dp[i]*2)

if result == 1:
    print(4)
else:
    print(result[-1])