A, B, C = map(int, input().split())
dp = [0]*100
for a in range(1, A+1):
    for b in range(1, B+1):
        for c in range(1, C+1):
            dp[a+b+c] += 1
print(dp.index(max(dp)))