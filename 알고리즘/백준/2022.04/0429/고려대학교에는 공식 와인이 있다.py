C, K, P = map(int, input().split())
result = 0
for c in range(1, C+1):
    result += K*c + P*c*c
print(result)
