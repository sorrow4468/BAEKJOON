import sys

input = sys.stdin.readline

N = int(input().rstrip())
T, P, dp = [], [], []
for i in range(N):
    a, b = map(int, input().rstrip().split())
    T.append(a)
    P.append(b)
    dp.append(b)
dp.append(0)
for i in range(N-1, -1, -1):
    if T[i]+i > N: # 이 날 시작한 일이 퇴사일을 넘길 경우
        dp[i] = dp[i+1]
    else: # 퇴사일 전에 일을 마칠 수 있는 경우
        # 그 일을 마친 날 기준, 해당 일에 얻을 수 있는 최대 이익
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
print(dp[0])

# https://www.acmicpc.net/problem/14501
# https://pacific-ocean.tistory.com/199