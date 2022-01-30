T = int(input())

for tc in range(T):
    N = int(input())

    dp = [0 for _ in range(N+1)]

    dp[1] = 1
    if N == 1:
        print(dp[1])
        continue
    dp[2] = 2

    if N == 2:
        print(dp[2])
        continue

    dp[3] = 4
    if N == 3:
        print(dp[3])
        continue

    if N > 3:
        for i in range(4, N+1):
            dp[i] = sum(dp[i-3:i])

        print(dp[N])