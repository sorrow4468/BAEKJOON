N = int(input())
try:
    records = list(map(int, input().split()))
    dp = [0]*101
    A = sum(records)/N
    for record in records:
        dp[record] += 1
    B = 0
    for i in range(101):
        if dp[i]:
            B += i * (dp[i]/N)
    print(f'{A/B:.2f}')
except:
    print('divide by zero')