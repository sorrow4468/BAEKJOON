H, Y = map(int, input().split())
dp = [0]*(Y+1)
dp[0] = H
for i in range(1, Y+1):
    if i-1 >= 0 and dp[i-1]:
        dp[i] = max(int(dp[i-1]*1.05), dp[i])
    if i-3 >= 0 and dp[i-3]:
        dp[i] = max(int(dp[i-3]*1.2), dp[i])
    if i-5 >= 0 and dp[i-5]:
        dp[i] = max(int(dp[i-5]*1.35), dp[i])
print(dp[Y])