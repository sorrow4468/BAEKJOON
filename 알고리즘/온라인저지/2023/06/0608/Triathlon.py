result = 0
for _ in range(int(input())):
    A, D, G = map(int, input().split())
    C = A*(D+G)
    if A == D+G:
        C *= 2
    result = max(result, C)
print(result)