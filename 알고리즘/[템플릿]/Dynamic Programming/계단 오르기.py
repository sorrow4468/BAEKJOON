N = int(input())
S = [0 for _ in range(301)] # stairs 
dp = [0 for _ in range(301)] # 미리 선언하여 N<=3 일 때 에러를 방지함
for i in range(N): S[i] = int(input())
dp[0] = S[0]
dp[1] = S[0] + S[1]
dp[2] = max(S[1]+S[2], S[0]+S[2])
for i in range(3, N):
    A = dp[i-3] + S[i-1] + S[i]
    B = dp[i-2] + S[i]
    dp[i] = max(A, B)
print(dp[N-1])

# https://www.acmicpc.net/problem/2579