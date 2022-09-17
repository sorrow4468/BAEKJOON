N = int(input())
result = [1] * N
for i in range(N):
    if i%2:
        result[i] += 1
if N%2:
    result[-1] = 3
print(*result)