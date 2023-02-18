result = 0
N = int(input())
tips = [int(input()) for _ in range(N)]
tips.sort(reverse=True)
for i in range(1, N+1):
    tip = tips[i-1]
    tip = tip - (i-1)
    if tip > 0: result += tip
print(result)