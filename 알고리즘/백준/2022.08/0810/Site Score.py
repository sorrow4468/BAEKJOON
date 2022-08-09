S = list(map(int, input().split()))
C = [56, 24, 14, 6]
result = 0
for i in range(4):
    result += S[i]*C[i]
    S *= 10
print(result)