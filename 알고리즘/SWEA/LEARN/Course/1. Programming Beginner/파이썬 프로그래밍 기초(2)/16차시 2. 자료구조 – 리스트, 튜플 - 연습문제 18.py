N, M = map(int, input().split(', '))

result = [[0 for _ in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        if result[i][j] == 0:
            result[i][j] = i*j

print(result)