dp = [0] * (101)
summ = 0
mode = 0
maxx = 0

for i in range(10):
    num = int(input())
    summ += num
    tmp = num//10
    dp[tmp] += 1
    if dp[tmp] > maxx:
        maxx = dp[tmp]
        mode = num

print(summ//10)
print(mode)
