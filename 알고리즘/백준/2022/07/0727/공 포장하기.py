B = list(map(int, input().split())) # balls
result = tmp = min(B)
for i in range(3):
    B[i] -= tmp
    if B[i]:
        result += B[i]//3
        B[i] = B[i]%3
L = [0, 1, 1, 2, 2] # left
result += L[sum(B)]
print(result)