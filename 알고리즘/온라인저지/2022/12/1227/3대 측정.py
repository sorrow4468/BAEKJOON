N, K, L = map(int, input().split())
result = [0, []]
for n in range(N):
    A, B, C = map(int, input().split())
    summ = A + B + C
    minn = min(A, B, C)
    if summ >= K and minn >= L:
        result[0] += 1
        result[1].append(A)
        result[1].append(B)
        result[1].append(C)
print(result[0])
print(*result[1])        