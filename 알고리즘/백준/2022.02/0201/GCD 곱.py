mod = 1000000007

N, M = map(int, input().split())

minn = min(N, M)

dp = [False, False] + [True] * minn

result = 1

for i in range(2, minn):
    if dp[i]:
        j = i
        while j <= minn:
            cnt = 0
            for k in range(i, minn, i):
                dp[k] = False
            cnt += (N//j) * (M//j)
            result = (result * (i**cnt)) % mod
            j *= i

print(result)