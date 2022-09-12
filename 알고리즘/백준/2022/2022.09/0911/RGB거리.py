N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, len(dp)):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])
print(min(dp[N-1]))

"""
DP문제 진짜 현타오네
코드가 이렇게 간단할 수가 있나
배열 그대로 들고 이동하면서
해당 집이 해당 색으로 집을 칠할 때의 
최소값들을 전부 구하면서 이동한다
"""