mod = 1000000007

N, M = map(int, input().split())

maxn = max(N, M)

dp = [False, False] + [True] * maxn

result = 1

for i in range(2, maxn):
    if dp[i]:
        j = i
        while j <= maxn:
            cnt = 0
            for k in range(i, maxn, i):
                dp[k] = False
            cnt += (N//j) * (M//j)
            result = (result * ((i**cnt)%mod)) % mod
            j *= i

print(result)