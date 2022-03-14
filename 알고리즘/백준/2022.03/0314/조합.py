N, M = map(int, input().split())

result = 1

for n in range(N, N-M, -1):
    result *= n

for m in range(1, M+1):
    result //= m

print(result)