N = input()
dp = [0]*9
for n in N:
    tmp = int(n)
    if tmp == 9:
        dp[6] += 1
    else:
        dp[tmp] += 1
if dp[6]%2: dp[6] += 1
dp[6] //= 2
print(max(dp))