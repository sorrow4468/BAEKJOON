P, K = map(int, input().split())
result = 'GOOD'
num = 0
for k in range(2, K):
    if P%k == 0:
        result = 'BAD'
        num = k
        break
if num:
    print(result, num)
else:
    print(result)