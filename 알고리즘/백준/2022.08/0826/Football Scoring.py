C = [6, 3, 2, 1, 2] # change
for _ in range(2):
    S = list(map(int, input().split())) # score
    result = 0
    for i in range(5): result += C[i] * S[i]
    print(result, end=' ')