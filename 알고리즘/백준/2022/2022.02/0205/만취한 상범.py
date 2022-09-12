T = int(input())

for t in range(T):
    N = int(input())

    dp = [True] * (N+1)
    dp[0] = False

    for i in range(2, N+1):
        for j in range(i, N+1, i):
            dp[j] = not dp[j]
    
    result = 0

    for d in dp:
        if d:
            result += 1
    
    print(result)